#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Spring15 backgrounds - ttbar
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
