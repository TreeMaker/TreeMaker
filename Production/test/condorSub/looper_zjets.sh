#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15v2

#### Spring15 backgrounds - zjets
SAMPLES=(
Spring15v2.DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.ZJetsToNuNu_HT-100To200_13TeV-madgraph \
Spring15v2.ZJetsToNuNu_HT-200To400_13TeV-madgraph \
Spring15v2.ZJetsToNuNu_HT-400To600_13TeV-madgraph \
Spring15v2.ZJetsToNuNu_HT-600ToInf_13TeV-madgraph \
Spring15v2.GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
