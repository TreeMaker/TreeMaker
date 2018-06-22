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
CMSSWVER=CMSSW_9_4_8
scram project ${CMSSWVER}
cd ${CMSSWVER}/src/
# cmsenv
eval `scramv1 runtime -sh`
git cms-init
git config gc.auto 0

# DeepAK8 setup
if [ "$ACCESS" = "https" ]; then echo "Needs your CERN username and password: NNKit is being cloned from gitlab"; fi
git clone ${ACCESS_GITLAB}DeepAK8/NNKit.git
cp NNKit/misc/mxnet_predict.xml $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/selected
scram setup mxnet_predict
cp NNKit/misc/lib/libmxnet_predict.so $CMSSW_BASE/external/$SCRAM_ARCH/lib/libmxnet_predict.so

# CMSSW patches
git cms-merge-topic TreeMaker:JERFormula942 # this one has dependencies (will be included in next 94X)
git cms-merge-topic -u TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_9_4_2
git cms-merge-topic -u TreeMaker:MET_942_FixEGdR # only for 2016 re-miniAOD MET egamma fix
git cms-merge-topic -u TreeMaker:storeJERFactorIndex942
git cms-merge-topic -u TreeMaker:AddJetAxis1_942
git cms-merge-topic -u TreeMaker:NjettinessAxis_942
git cms-merge-topic -u TreeMaker:SpeedupPuppi948 # will be included in next 94X

# outside repositories
git clone ${ACCESS_GITHUB}TreeMaker/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
git clone ${ACCESS_GITHUB}kpedro88/CondorProduction.git Condor/Production
git clone ${ACCESS_GITHUB}${FORK}/TreeMaker.git -b ${BRANCH}

# compile
scram b -j ${CORES}

# extra setup
cd TreeMaker/Production/test/condorSub/
python $CMSSW_BASE/src/Condor/Production/python/linkScripts.py
ln -s ${CMSSW_BASE}/src/NNKit/data/ak8/full/preprocessing.json ${CMSSW_BASE}/src/TreeMaker/Production/test/data/.
ln -s ${CMSSW_BASE}/src/NNKit/data/ak8/full/resnet-symbol.json ${CMSSW_BASE}/src/TreeMaker/Production/test/data/.
ln -s ${CMSSW_BASE}/src/NNKit/data/ak8/full/resnet.params ${CMSSW_BASE}/src/TreeMaker/Production/test/data/.
