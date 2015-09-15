#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Spring15 backgrounds - zjets
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZJetsToNuNu_HT-100To200_13TeV-madgraph
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZJetsToNuNu_HT-200To400_13TeV-madgraph
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZJetsToNuNu_HT-400To600_13TeV-madgraph
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZJetsToNuNu_HT-600ToInf_13TeV-madgraph
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
