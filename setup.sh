#!/bin/bash -e

usage(){
	EXIT=$1

	echo "setup.sh [options]"
	echo ""
	echo "-f [fork]           clone from specified fork (default = TreeMaker)"
	echo "-b [branch]         clone specified branch (default = Run2_2018_prompt)"
	echo "-a [protocol]       use protocol to clone (default = ssh, alternative = https)"
	echo "-j [cores]          run CMSSW compilation on # cores (default = 8)"
	echo "-l                  link to mxnet library from cvmfs (default = use local version)"
	echo "-h                  display this message and exit"

	exit $EXIT
}

FORK=TreeMaker
BRANCH=Run2_2018_prompt
ACCESS=ssh
CORES=8
LINKMXNET=""

# process options
while getopts "f:b:a:j:lh" opt; do
	case "$opt" in
	f) FORK=$OPTARG
	;;
	b) BRANCH=$OPTARG
	;;
	a) ACCESS=$OPTARG
	;;
	j) CORES=$OPTARG
	;;
	l) LINKMXNET=true
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
CMSSWVER=CMSSW_10_1_7
scram project ${CMSSWVER}
cd ${CMSSWVER}/src/
# cmsenv
eval `scramv1 runtime -sh`
git cms-init
git config gc.auto 0

# DeepAK8 setup
if [ "$ACCESS" = "https" ]; then echo "Needs your CERN username and password: NNKit is being cloned from gitlab"; fi
git clone ${ACCESS_GITLAB}TreeMaker/NNKit.git -b avoid_exceptions
if [ -n "$LINKMXNET" ]; then
	cp /cvmfs/cms-lpc.opensciencegrid.org/sl6/opt/mxnet-1.1.0/mxnet_predict.xml $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/selected
	scram setup mxnet_predict
else
	cp NNKit/misc/mxnet_predict.xml $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/selected
	scram setup mxnet_predict
	cp --remove-destination NNKit/misc/lib/libmxnet_predict.so $CMSSW_BASE/external/$SCRAM_ARCH/lib/libmxnet_predict.so
fi

# CMSSW patches
git cms-merge-topic TreeMaker:JERFormula1017 # this one has dependencies (will be included in next 94X)
git cms-merge-topic -u TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_10_1_7
git cms-merge-topic -u TreeMaker:storeJERFactorIndex1017
git cms-merge-topic -u TreeMaker:AddJetAxis1_1017
git cms-merge-topic -u TreeMaker:NjettinessAxis_1017
git cms-merge-topic -u TreeMaker:SpeedupPuppi1017 # will be included in next 94X

# outside repositories
git clone ${ACCESS_GITHUB}TreeMaker/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
git clone ${ACCESS_GITHUB}kpedro88/CondorProduction.git Condor/Production
git clone ${ACCESS_GITHUB}${FORK}/TreeMaker.git -b ${BRANCH}

# compile
scram b -j ${CORES}

# extra setup
cd TreeMaker/Production/test/condorSub/
python $CMSSW_BASE/src/Condor/Production/python/linkScripts.py
DEEPDATA=${CMSSW_BASE}/src/NNKit/data/ak8/full
TMDATA=${CMSSW_BASE}/src/TreeMaker/Production/test/data
cp ${DEEPDATA}/preprocessing.json ${TMDATA}/
cp ${DEEPDATA}/resnet-symbol.json ${TMDATA}/
cp ${DEEPDATA}/resnet.params ${TMDATA}/
