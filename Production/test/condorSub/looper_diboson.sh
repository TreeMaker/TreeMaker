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

#### Spring16 rare backgrounds - diboson
SAMPLES=(
Spring16.WWTo2L2Nu_13TeV-powheg \
Spring16.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring16.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring16.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring16.ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring16.ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring16.WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring16.ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring16.WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
