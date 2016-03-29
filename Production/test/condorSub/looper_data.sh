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

#### Run2015C Prompt RECO
SCENARIO=re2015C
SAMPLES=(
Run2015C_25ns-05Oct2015-v1.DoubleEG \
Run2015C_25ns-05Oct2015-v1.DoubleMuon \
Run2015C_25ns-05Oct2015-v1.HTMHT \
Run2015C_25ns-05Oct2015-v1.JetHT \
Run2015C_25ns-05Oct2015-v1.MET \
Run2015C_25ns-05Oct2015-v1.SingleElectron \
Run2015C_25ns-05Oct2015-v1.SingleMuon \
Run2015C_25ns-05Oct2015-v1.SinglePhoton
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2015D re-miniAOD (part 1)
SCENARIO=re2015D
SAMPLES=(
Run2015D-05Oct2015-v1.DoubleEG \
Run2015D-05Oct2015-v1.DoubleMuon \
Run2015D-05Oct2015-v1.HTMHT \
Run2015D-05Oct2015-v1.JetHT \
Run2015D-05Oct2015-v1.MET \
Run2015D-05Oct2015-v1.SingleElectron \
Run2015D-05Oct2015-v1.SingleMuon \
Run2015D-05Oct2015-v1.SinglePhoton
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done

#### Run2015D Prompt RECO (part 2)
SCENARIO=2015Db
SAMPLES=(
Run2015D-PromptReco-v4.DoubleEG \
Run2015D-PromptReco-v4.DoubleMuon \
Run2015D-PromptReco-v4.HTMHT \
Run2015D-PromptReco-v4.JetHT \
Run2015D-PromptReco-v4.MET \
Run2015D-PromptReco-v4.SingleElectron \
Run2015D-PromptReco-v4.SingleMuon \
Run2015D-PromptReco-v4.SinglePhoton
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE} -d
done
