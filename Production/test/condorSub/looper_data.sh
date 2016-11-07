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


#### Run2016C Prompt RECO
SCENARIO=2016CD
SAMPLES=(
Run2016C-PromptReco-v2.HTMHT \
Run2016C-PromptReco-v2.JetHT \
Run2016C-PromptReco-v2.MET \
Run2016C-PromptReco-v2.SingleElectron \
Run2016C-PromptReco-v2.SingleMuon \
Run2016C-PromptReco-v2.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016D Prompt RECO
SCENARIO=2016CD
SAMPLES=(
Run2016D-PromptReco-v2.HTMHT \
Run2016D-PromptReco-v2.JetHT \
Run2016D-PromptReco-v2.MET \
Run2016D-PromptReco-v2.SingleElectron \
Run2016D-PromptReco-v2.SingleMuon \
Run2016D-PromptReco-v2.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016E Prompt RECO
SCENARIO=2016EF
SAMPLES=(
Run2016E-PromptReco-v2.HTMHT \
Run2016E-PromptReco-v2.JetHT \
Run2016E-PromptReco-v2.MET \
Run2016E-PromptReco-v2.SingleElectron \
Run2016E-PromptReco-v2.SingleMuon \
Run2016E-PromptReco-v2.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016F Prompt RECO
SCENARIO=2016EF
SAMPLES=(
Run2016F-PromptReco-v1.HTMHT \
Run2016F-PromptReco-v1.JetHT \
Run2016F-PromptReco-v1.MET \
Run2016F-PromptReco-v1.SingleElectron \
Run2016F-PromptReco-v1.SingleMuon \
Run2016F-PromptReco-v1.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016G Prompt RECO
SCENARIO=2016G
SAMPLES=(
Run2016G-PromptReco-v1.HTMHT \
Run2016G-PromptReco-v1.JetHT \
Run2016G-PromptReco-v1.MET \
Run2016G-PromptReco-v1.SingleElectron \
Run2016G-PromptReco-v1.SingleMuon \
Run2016G-PromptReco-v1.SinglePhoton \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2016H Prompt RECO
SCENARIO=2016H
SAMPLES=(
Run2016H-PromptReco-v1.HTMHT \
Run2016H-PromptReco-v1.JetHT \
Run2016H-PromptReco-v1.MET \
Run2016H-PromptReco-v1.SingleElectron \
Run2016H-PromptReco-v1.SingleMuon \
Run2016H-PromptReco-v1.SinglePhoton \
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
