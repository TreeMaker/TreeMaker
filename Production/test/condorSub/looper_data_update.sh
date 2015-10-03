#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Run2015D Prompt RECO
SCENARIO=2015D
SAMPLES=(
Run2015D-PromptReco-v3.DoubleEG \
Run2015D-PromptReco-v3.DoubleMuon \
Run2015D-PromptReco-v3.HTMHT \
Run2015D-PromptReco-v3.JetHT \
Run2015D-PromptReco-v3.MET \
Run2015D-PromptReco-v3.SingleElectron \
Run2015D-PromptReco-v3.SingleMuon \
Run2015D-PromptReco-v3.SinglePhoton
)
JOBSTART=(
78 \
40 \
30 \
76 \
29 \
95 \
60 \
40
)

for ((i=0; i < ${#SAMPLES[@]}; i++)); do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLES[$i]} -d -j ${JOBSTART[$i]}
done
