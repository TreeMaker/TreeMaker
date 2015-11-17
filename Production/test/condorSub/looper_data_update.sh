#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Run2015D Prompt RECO
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
JOBSTART=(
384 \
190 \
94 \
242 \
82 \
456 \
329 \
143
)

for ((i=0; i < ${#SAMPLES[@]}; i++)); do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLES[$i]} -d -j ${JOBSTART[$i]}
done
