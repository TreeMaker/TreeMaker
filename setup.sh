#!/bin/bash -e

CMSSWVER=CMSSW_10_2_21
FORK=TreeMaker
BRANCH=Run2_2017
ACCESS=ssh
CORES=8
NAME=""
DIR="${PWD}"
BATCH=""

usage(){
	EXIT=$1

	echo "setup.sh [options]"
	echo ""
	echo "-f [fork]           clone from specified fork (default = ${FORK})"
	echo "-b [branch]         clone specified branch (default = ${BRANCH})"
	echo "-B                  configure some settings for checkout within batch setups (default = ${BATCH})"
	echo "-c [version]        use specified CMSSW version (default = ${CMSSWVER})"
	echo "-a [protocol]       use protocol to clone (default = ${ACCESS}, alternative = https)"
	echo "-j [cores]          run CMSSW compilation on # cores (default = ${CORES})"
	echo "-n [name]           name of the CMSSW directory (default = ${CMSSWVER})"
	echo "-d [dir]            project installation area for the CMSSW directory (default = ${DIR})"
	echo "-h                  display this message and exit"

	exit $EXIT
}

# process options
while getopts "f:b:Ba:j:n:d:c:h" opt; do
	case "$opt" in
	f) FORK=$OPTARG
	;;
	b) BRANCH=$OPTARG
	;;
	B) BATCH=--upstream-only
	;;
	c) CMSSWVER=$OPTARG
	;;
	a) ACCESS=$OPTARG
	;;
	j) CORES=$OPTARG
	;;
	n) NAME=$OPTARG
	;;
	d) DIR=$OPTARG
	;;
	h) usage 0
	;;
	esac
done

# check options
if [ "$ACCESS" = "ssh" ]; then
	ACCESS_GITHUB=git@github.com:
	ACCESS_GITLAB=ssh://git@gitlab.cern.ch:7999/
	ACCESS_CMSSW=--ssh
elif [ "$ACCESS" = "https" ]; then
	ACCESS_GITHUB=https://github.com/
	ACCESS_GITLAB=https://gitlab.cern.ch/
	ACCESS_CMSSW=--https
else
	usage 1
fi

# make sure that scram is available in a batch situation when an interactive terminal might not be available
if [[ -n "$BATCH" ]]; then
	echo "WARNING: Non-interactive shell found!"
	if [[ -f "${HOME}/.bashrc" ]]; then
		echo "Sourcing the .bashrc file"
		source ${HOME}/.bashrc
	fi
	if [[ -f "/cvmfs/cms.cern.ch/cmsset_default.sh" ]]; then
		echo -e "cms.cern.ch is accessible\n\t==> source /cvmfs/cms.cern.ch/cmsset_default.sh\n"
		source /cvmfs/cms.cern.ch/cmsset_default.sh
	fi
fi

# get CMSSW release
if [[ "$CMSSWVER" == "CMSSW_10_2_"* ]]; then
	GCC_VERSION=gcc700
else
	echo "Unsupported CMSSW version: $CMSSWVER"
	exit 1
fi

if [[ `uname -r` == *"el6"* ]]; then
	SLC_VERSION="slc6"
elif [[ `uname -r` == *"el7"* ]]; then
	SLC_VERSION="slc7"
elif [[ -f "/etc/redhat-release" ]]; then
	VERSION_TMP=`awk -F'[ .]' '{print $4}' "/etc/redhat-release"`
	POSSIBLE_VERSIONS=( 6 7 )
	if [[ "${POSSIBLE_VERSIONS[@]} " =~ " ${VERSION_TMP}" ]]; then
		SLC_VERSION="slc${VERSION_TMP}"
	else
		echo "WARNING::Unknown SLC version. Defaulting to SLC6."
		SLC_VERSION="slc6"
	fi
else
	echo "WARNING::Unknown SLC version. Defaulting to SLC6."
	SLC_VERSION="slc6"
fi
export SCRAM_ARCH=${SLC_VERSION}_amd64_${GCC_VERSION}

# cmsrel
SCRAM_PROJECT_OPTIONS=""
if [ "$DIR" != "${PWD}" ]; then
	SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS --dir ${DIR}"
fi
if [ "$NAME" != "" ]; then
	SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS --name ${NAME}"
else
	NAME=${CMSSWVER}
fi
SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS ${CMSSWVER}"
scram project ${SCRAM_PROJECT_OPTIONS}
cd ${DIR}/${NAME}/src

# cmsenv
eval `scramv1 runtime -sh`
git cms-init $ACCESS_CMSSW $BATCH
git config gc.auto 0

# batch git config
if [[ -n "$BATCH" ]]; then
	git config --global --add user.name "TreeMaker GitHub"
	git config --global --add user.email "treemaker@github.com"
	git config --global --add user.github "TreeMaker"
fi

# CMSSW patches
if [[ "$CMSSWVER" == "CMSSW_10_2_"* ]]; then
	git cms-merge-topic -u $ACCESS_CMSSW TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_10_2_7
	git cms-merge-topic -u $ACCESS_CMSSW TreeMaker:storeJERFactorIndex10220
	git cms-merge-topic -u $ACCESS_CMSSW TreeMaker:AddJetAxis1_1027
	git cms-merge-topic -u $ACCESS_CMSSW TreeMaker:DeepAK8v2_10221
fi

# outside repositories
git clone ${ACCESS_GITHUB}TreeMaker/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
git clone ${ACCESS_GITHUB}kpedro88/CondorProduction.git Condor/Production
git clone ${ACCESS_GITHUB}${FORK}/TreeMaker.git -b ${BRANCH}

# compile
scram b -j ${CORES}

# extra setup
cd TreeMaker/Production/test/condorSub/
python $CMSSW_BASE/src/Condor/Production/python/linkScripts.py
