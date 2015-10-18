#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15v2

#### Spring15 backgrounds - ttbar
SAMPLES=(
Spring15v2.TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring15v2.TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring15v2.TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring15v2.TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
