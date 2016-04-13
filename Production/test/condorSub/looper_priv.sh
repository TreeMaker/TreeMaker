#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15Fastv2

#### privately generated SMS
SAMPLES=(
PrivateSamples.SMS-T1ttbb_mGluino-1300_mLSP-5_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_cff \
PrivateSamples.SMS-T1ttbb_mGluino-1300_mLSP-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_cff \
PrivateSamples.SMS-T2tt_mStop-170_mLSP-1_2bd_madgraphMLM-pythia8_13TeV \
PrivateSamples.SMS-T2tt_mStop-170_mLSP-1_madgraphMLM-pythia8_13TeV \
PrivateSamples.SMS-T2tt_mStop-172_mLSP-1_madgraphMLM-pythia8_13TeV \
PrivateSamples.SMS-T2tt_mStop-173_mLSP-1_madgraphMLM-pythia8_13TeV \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
