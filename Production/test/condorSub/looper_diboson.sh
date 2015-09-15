#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Spring15 rare backgrounds - diboson
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WWToLNuQQ_13TeV-powheg
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WWTo2L2Nu_13TeV-powheg
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8
