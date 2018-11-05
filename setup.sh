#!/bin/bash -e

usage(){
	EXIT=$1

	echo "setup.sh [options]"
	echo ""
	echo "-f [fork]           clone from specified fork (default = TreeMaker)"
	echo "-b [branch]         clone specified branch (default = Run2_2017)"
	echo "-a [protocol]       use protocol to clone (default = ssh, alternative = https)"
	echo "-j [cores]          run CMSSW compilation on # cores (default = 8)"
	echo "-h                  display this message and exit"

	exit $EXIT
}

FORK=TreeMaker
BRANCH=Run2_2017
ACCESS=ssh
CORES=8

# process options
while getopts "f:b:a:j:h" opt; do
	case "$opt" in
	f) FORK=$OPTARG
	;;
	b) BRANCH=$OPTARG
	;;
	a) ACCESS=$OPTARG
	;;
	j) CORES=$OPTARG
	;;
	h) usage 0
	;;
	esac
done

# check options
if [ "$ACCESS" = "ssh" ]; then
	ACCESS_GITHUB=git@github.com:
	ACCESS_GITLAB=ssh://git@gitlab.cern.ch:7999/
elif [ "$ACCESS" = "https" ]; then
	ACCESS_GITHUB=https://github.com/
	ACCESS_GITLAB=https://gitlab.cern.ch/
else
	usage 1
fi

# get CMSSW release
export SCRAM_ARCH=slc6_amd64_gcc630
# cmsrel
CMSSWVER=CMSSW_9_4_11
scram project ${CMSSWVER}
cd ${CMSSWVER}/src/
# cmsenv
eval `scramv1 runtime -sh`
git cms-init
git config gc.auto 0

# CMSSW patches
git cms-merge-topic TreeMaker:fixFormulaEvaluator_949 # this one has dependencies, might be in a future 9_4_X release
git cms-merge-topic -u TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_9_4_2
git cms-merge-topic -u TreeMaker:storeJERFactorIndex942
git cms-merge-topic -u TreeMaker:AddJetAxis1_942
git cms-merge-topic -u TreeMaker:NjettinessAxis_948
git cms-merge-topic -u TreeMaker:METFixEE2017_949

# outside repositories
git clone ${ACCESS_GITHUB}TreeMaker/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
git clone ${ACCESS_GITHUB}kpedro88/CondorProduction.git Condor/Production
git clone ${ACCESS_GITHUB}${FORK}/TreeMaker.git -b ${BRANCH}

# compile
scram b -j ${CORES}

# extra setup
cd TreeMaker/Production/test/condorSub/
python $CMSSW_BASE/src/Condor/Production/python/linkScripts.py
