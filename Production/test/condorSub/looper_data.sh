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

#### global ReReco scenario
SCENARIO=2016ReReco23Sep

#### Run2016B ReReco
SAMPLES=(
Run2016B-23Sep2016-v3.HTMHT \
Run2016B-23Sep2016-v3.JetHT \
Run2016B-23Sep2016-v3.MET \
Run2016B-23Sep2016-v3.SingleElectron \
Run2016B-23Sep2016-v3.SingleMuon \
Run2016B-23Sep2016-v3.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done


#### Run2016C ReReco
SAMPLES=(
Run2016C-23Sep2016-v1.HTMHT \
Run2016C-23Sep2016-v1.JetHT \
Run2016C-23Sep2016-v1.MET \
Run2016C-23Sep2016-v1.SingleElectron \
Run2016C-23Sep2016-v1.SingleMuon \
Run2016C-23Sep2016-v1.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016D ReReco
SAMPLES=(
Run2016D-23Sep2016-v1.HTMHT \
Run2016D-23Sep2016-v1.JetHT \
Run2016D-23Sep2016-v1.MET \
Run2016D-23Sep2016-v1.SingleElectron \
Run2016D-23Sep2016-v1.SingleMuon \
Run2016D-23Sep2016-v1.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016E ReReco
SAMPLES=(
Run2016E-23Sep2016-v1.HTMHT \
Run2016E-23Sep2016-v1.JetHT \
Run2016E-23Sep2016-v1.MET \
Run2016E-23Sep2016-v1.SingleElectron \
Run2016E-23Sep2016-v1.SingleMuon \
Run2016E-23Sep2016-v1.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016F ReReco
SAMPLES=(
Run2016F-23Sep2016-v1.HTMHT \
Run2016F-23Sep2016-v1.JetHT \
Run2016F-23Sep2016-v1.MET \
Run2016F-23Sep2016-v1.SingleElectron \
Run2016F-23Sep2016-v1.SingleMuon \
Run2016F-23Sep2016-v1.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016G ReReco
SAMPLES=(
Run2016G-23Sep2016-v1.HTMHT \
Run2016G-23Sep2016-v1.JetHT \
Run2016G-23Sep2016-v1.MET \
Run2016G-23Sep2016-v1.SingleElectron \
Run2016G-23Sep2016-v1.SingleMuon \
Run2016G-23Sep2016-v1.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016H Prompt RECO
SCENARIO=2016H
SAMPLES=(
Run2016H-PromptReco-v2.HTMHT \
Run2016H-PromptReco-v2.JetHT \
Run2016H-PromptReco-v2.MET \
Run2016H-PromptReco-v2.SingleElectron \
Run2016H-PromptReco-v2.SingleMuon \
Run2016H-PromptReco-v2.SinglePhoton \
Run2016H-PromptReco-v3.HTMHT \
Run2016H-PromptReco-v3.JetHT \
Run2016H-PromptReco-v3.MET \
Run2016H-PromptReco-v3.SingleElectron \
Run2016H-PromptReco-v3.SingleMuon \
Run2016H-PromptReco-v3.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done
