#!/bin/bash

FORK=TreeMaker
BRANCH=Run2

while getopts "f:b:" opt; do
	case "$opt" in
	f) FORK=$OPTARG
	;;
	b) BRANCH=$OPTARG
	;;
	esac
done

export SCRAM_ARCH=slc6_amd64_gcc530
# cmsrel
scram project CMSSW_8_0_28
cd CMSSW_8_0_28/src/
$ cmsenv
eval `scramv1 runtime -sh`
git cms-init
git remote add btv-cmssw https://github.com/cms-btv-pog/cmssw.git
git fetch btv-cmssw refs/tags/BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_8_0_21
git cms-merge-topic -u cms-btv-pog:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_8_0_21
git cms-merge-topic -u kpedro88:storeJERFactor8028
git cms-merge-topic -u kpedro88:badMuonFilters_80X_v2_RA2
git cms-merge-topic -u kpedro88:FixMetSigData8028
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_80X_V3
git clone git@github.com:kpedro88/CondorProduction.git Condor/Production  
git clone git@github.com:${FORK}/TreeMaker.git -b ${BRANCH}
scram b -j 8
cd TreeMaker/Production/test/condorSub/
ln -s $CMSSW_BASE/src/Condor/Production/scripts/* .
