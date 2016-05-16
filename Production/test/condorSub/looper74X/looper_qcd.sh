#!/bin/bash

CHECKARGS=""
OUTPUTDIR=""

#check arguments
while getopts "kd:" opt; do
  case "$opt" in
  k) CHECKARGS="${CHECKARGS} -k"
    ;;
  d) OUTPUTDIR=$OPTARG
    ;;
  esac
done

if [ -z "$OUTPUTDIR" ]; then
  echo "Need to specify output directory with -d"
  exit  
fi

./FScheck.sh ${CHECKARGS}

SCENARIO=Spring15v2

#### Spring15 backgrounds - QCD
SAMPLES=(
Spring15v2.QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15v2.QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
