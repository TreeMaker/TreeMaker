#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15Fastv2

#### privately generated T1ttbb
SAMPLES=(
PrivateSamples.SMS-T1ttbb_mGluino-1300_mLSP-5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_cff \
PrivateSamples.SMS-T1ttbb_mGluino-1300_mLSP-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_cff \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
