#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Run2015B Prompt RECO
SCENARIO=2015B
SAMPLES="
Run2015B-PromptReco-v1.DoubleEG \
Run2015B-PromptReco-v1.DoubleMuon \
Run2015B-PromptReco-v1.HTMHT \
Run2015B-PromptReco-v1.SingleElectron \
Run2015B-PromptReco-v1.SingleMuon \
Run2015B-PromptReco-v1.SinglePhoton
"

for SAMPLE in ${SAMPLES}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done

#### Run2015B July 17 reprocessing
SCENARIO=re2015B
SAMPLES="
Run2015B-17Jul2015-v1.DoubleEG \
Run2015B-17Jul2015-v1.DoubleMuon \
Run2015B-17Jul2015-v1.EGamma \
Run2015B-17Jul2015-v1.HTMHT \
Run2015B-17Jul2015-v1.SingleElectron \
Run2015B-17Jul2015-v1.SingleMuon \
Run2015B-17Jul2015-v1.SinglePhoton
"

for SAMPLE in ${SAMPLES}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done

#### Run2015C Prompt RECO
SCENARIO=2015C
SAMPLES="
Run2015C-PromptReco-v1.DoubleEG \
Run2015C-PromptReco-v1.DoubleMuon \
Run2015C-PromptReco-v1.HTMHT \
Run2015C-PromptReco-v1.SingleElectron \
Run2015C-PromptReco-v1.SingleMuon \
Run2015C-PromptReco-v1.SinglePhoton
"

for SAMPLE in ${SAMPLES}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done

