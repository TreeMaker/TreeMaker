#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15

#### Spring15 rare backgrounds - tt/H+X
SAMPLES="
Spring15.WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15.ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15.ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8 \
Spring15.TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Spring15.TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Spring15.TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring15.TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext1 \
Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext2 \
Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8_ext3
"

for SAMPLE in ${SAMPLES}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
