#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15Fastv2

#### privately generated T5HH
SAMPLES=(
PrivateSamples.SMS-T5HH_mGluino-1200_mLSP-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_cff \
PrivateSamples.SMS-T5HH_mGluino-1200_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_cff \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
