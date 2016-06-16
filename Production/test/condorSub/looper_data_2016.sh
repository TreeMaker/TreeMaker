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

#### Run2016B Prompt RECO
SCENARIO=2016B
SAMPLES=(
Run2016B-PromptReco-v2.HTMHT \
Run2016B-PromptReco-v2.JetHT \
Run2016B-PromptReco-v2.MET \
Run2016B-PromptReco-v2.SingleElectron \
Run2016B-PromptReco-v2.SingleMuon \
Run2016B-PromptReco-v2.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done
