#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Run2015B Prompt RECO
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.DoubleEG
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.DoubleMuon
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.HTMHT
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.SingleElectron
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.SingleMuon
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.SinglePhoton

#### Run2015B July 17 reprocessing
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.DoubleEG
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.DoubleMuon
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.EGamma
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.HTMHT
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.SingleElectron
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.SingleMuon
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.SinglePhoton

#### Run2015C Prompt RECO
python generateSubmission.py -n 1 -s -o $outputDir -c 2015C -f Run2015C-PromptReco-v1.DoubleEG
python generateSubmission.py -n 1 -s -o $outputDir -c 2015C -f Run2015C-PromptReco-v1.DoubleMuon
python generateSubmission.py -n 1 -s -o $outputDir -c 2015C -f Run2015C-PromptReco-v1.HTMHT
python generateSubmission.py -n 1 -s -o $outputDir -c 2015C -f Run2015C-PromptReco-v1.SingleElectron
python generateSubmission.py -n 1 -s -o $outputDir -c 2015C -f Run2015C-PromptReco-v1.SingleMuon
python generateSubmission.py -n 1 -s -o $outputDir -c 2015C -f Run2015C-PromptReco-v1.SinglePhoton
