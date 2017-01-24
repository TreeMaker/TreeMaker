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

SCENARIO=Summer16

#### Summer16 rare backgrounds - tt/H+X
SAMPLES=(
Summer16.TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_ext1 \
Summer16.TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Summer16.TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_ext1 \
Summer16.TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_ext2 \
Summer16.TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Summer16.TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8 \
Summer16.TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_ext1 \
Summer16.TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
