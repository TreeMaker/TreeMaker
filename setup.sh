#!/bin/bash

FORK=TreeMaker
BRANCH=Run2_2017

while getopts "f:b:" opt; do
	case "$opt" in
	f) FORK=$OPTARG
	;;
	b) BRANCH=$OPTARG
	;;
	esac
done

export SCRAM_ARCH=slc6_amd64_gcc630
# cmsrel
CMSSWVER=CMSSW_9_4_8
scram project ${CMSSWVER}
cd ${CMSSWVER}/src/
# cmsenv
eval `scramv1 runtime -sh`
git cms-init
git cms-merge-topic TreeMaker:JERFormula942 # this one has dependencies
git cms-merge-topic -u TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_9_4_2
git cms-merge-topic -u TreeMaker:MET_942_FixEGdR
git cms-merge-topic -u TreeMaker:storeJERFactorIndex942
git cms-merge-topic -u TreeMaker:AddJetAxis1_942
git cms-merge-topic -u TreeMaker:NjettinessAxis_942
git cms-merge-topic -u TreeMaker:SpeedupPuppi948
git clone git@github.com:TreeMaker/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
git clone git@github.com:kpedro88/CondorProduction.git Condor/Production  
git clone git@github.com:${FORK}/TreeMaker.git -b ${BRANCH}
scram b -j 8
cd TreeMaker/Production/test/condorSub/
python $CMSSW_BASE/src/Condor/Production/python/linkScripts.py
