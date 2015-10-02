#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15

#### Spring15 backgrounds - QCD
SAMPLES=(
Spring15.QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15.QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15.QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15.QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15.QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15.QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15.QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
