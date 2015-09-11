#!/bin/bash

KEEPTAR=$1

./FScheck.sh "$KEEPTAR"

#### Spring15 negative-weight samples
python generateSubmissionNeff.py -s -f Spring15.ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring15.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring15.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring15.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring15.WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring15.ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext1
python generateSubmissionNeff.py -s -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext2
python generateSubmissionNeff.py -s -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext3
python generateSubmissionNeff.py -s -f Spring15.TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8
python generateSubmissionNeff.py -s -f Spring15.TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8
python generateSubmissionNeff.py -s -f Spring15.TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8
python generateSubmissionNeff.py -s -f Spring15.TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8
