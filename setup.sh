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
git config gc.auto 0
echo "Needs your CERN username and password: NNKit is being cloned from gitlab"
git clone https://gitlab.cern.ch/DeepAK8/NNKit.git
cp NNKit/misc/mxnet_predict.xml $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/selected
scram setup mxnet_predict
cp NNKit/misc/lib/libmxnet_predict.so $CMSSW_BASE/external/$SCRAM_ARCH/lib/libmxnet_predict.so
git cms-merge-topic TreeMaker:JERFormula942 # this one has dependencies (will be included in next 94X)
git cms-merge-topic -u TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_9_4_2
git cms-merge-topic -u TreeMaker:MET_942_FixEGdR # only for 2016 re-miniAOD MET egamma fix
git cms-merge-topic -u TreeMaker:storeJERFactorIndex942
git cms-merge-topic -u TreeMaker:AddJetAxis1_942
git cms-merge-topic -u TreeMaker:NjettinessAxis_942
git cms-merge-topic -u TreeMaker:SpeedupPuppi948 # will be included in next 94X
git clone git@github.com:TreeMaker/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
git clone git@github.com:kpedro88/CondorProduction.git Condor/Production  
git clone git@github.com:${FORK}/TreeMaker.git -b ${BRANCH}
scram b -j 8
cd TreeMaker/Production/test/condorSub/
python $CMSSW_BASE/src/Condor/Production/python/linkScripts.py
ln -s ${CMSSW_BASE}/src/NNKit/data/ak8/full/preprocessing.json ${CMSSW_BASE}/src/TreeMaker/Production/test/data/.
ln -s ${CMSSW_BASE}/src/NNKit/data/ak8/full/resnet-symbol.json ${CMSSW_BASE}/src/TreeMaker/Production/test/data/.
ln -s ${CMSSW_BASE}/src/NNKit/data/ak8/full/resnet.params ${CMSSW_BASE}/src/TreeMaker/Production/test/data/.
