#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Spring15 backgrounds - QCD
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8
#python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
