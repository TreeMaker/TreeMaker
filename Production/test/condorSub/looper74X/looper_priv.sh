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

SCENARIO=Spring15Fastv2sig

#### privately generated T5HH & T1ttbb
SAMPLES=(
PrivateSamples.SMS-T5HH_mGluino-1200_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
PrivateSamples.SMS-T5HH_mGluino-1200_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
PrivateSamples.SMS-T1ttbb_mGluino-1300_mLSP-5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
PrivateSamples.SMS-T1ttbb_mGluino-1300_mLSP-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
