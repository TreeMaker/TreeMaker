#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### squark
#python generateSubmission.py -o $outputDir -c Phys14 -n 1 -s -f PHYS14.SMS-T2bb_2J_mStop-600_mLSP-580_Tune4C_13TeV-madgraph-tauola
#python generateSubmission.py -o $outputDir -c Phys14 -n 1 -s -f PHYS14.SMS-T2bb_2J_mStop-900_mLSP-100_Tune4C_13TeV-madgraph-tauola
#python generateSubmission.py -o $outputDir -c Phys14 -n 1 -s -f PHYS14.SMS-T2qq_2J_mStop-1200_mLSP-100_Tune4C_13TeV-madgraph-tauola
#python generateSubmission.py -o $outputDir -c Phys14 -n 1 -s -f PHYS14.SMS-T2qq_2J_mStop-600_mLSP-550_Tune4C_13TeV-madgraph-tauola

#### Spring15 gluino
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
