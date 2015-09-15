#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Spring15 rare backgrounds - tt/H+X
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext2
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext3
