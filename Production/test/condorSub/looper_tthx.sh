#!/bin/bash

CHECKARGS=""
OUTPUTDIR=""

#check arguments
while getopts "kd:" opt; do
  case "$opt" in
  k) CHECKARGS="${CHECKARGS} -k"
    ;;
  d) OUTPUTDIR=$OPTARG
    ;;
  esac
done

if [ -z "$OUTPUTDIR" ]; then
  echo "Need to specify output directory with -d"
  exit  
fi

./FScheck.sh ${CHECKARGS}

SCENARIO=Spring16

#### Spring16 rare backgrounds - tt/H+X
SAMPLES=(
Spring16.TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring16.TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring16.TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Spring16.TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Spring16.TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Spring16.TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8_ext1 \
)

#missing:
#Spring16.WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
#Spring16.ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8 \
#Spring16.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8 \

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
