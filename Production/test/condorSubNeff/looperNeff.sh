#!/bin/bash


CHECKARGS=""

#check arguments
while getopts "k" opt; do
  case "$opt" in
  k) CHECKARGS="${CHECKARGS} -k"
    ;;
  esac
done

./FScheck.sh ${CHECKARGS}

#### Spring16 negative-weight samples
python generateSubmissionNeff.py -s -f Spring16.ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1
python generateSubmissionNeff.py -s -f Spring16.TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8
python generateSubmissionNeff.py -s -f Spring16.TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8_ext1
python generateSubmissionNeff.py -s -f Spring16.TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8
python generateSubmissionNeff.py -s -f Spring16.TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8
python generateSubmissionNeff.py -s -f Spring16.TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8
python generateSubmissionNeff.py -s -f Spring16.TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8
python generateSubmissionNeff.py -s -f Spring16.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring16.WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8
python generateSubmissionNeff.py -s -f Spring16.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring16.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring16.WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8
python generateSubmissionNeff.py -s -f Spring16.ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring16.ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmissionNeff.py -s -f Spring16.ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8
