#!/bin/bash

CHECKARGS=""
OUTDIR=""

#check arguments
while getopts "kd:" opt; do
  case "$opt" in
  k) CHECKARGS="${CHECKARGS} -k"
    ;;
  d) OUTDIR=$OPTARG
    ;;
  esac
done

if [ -z "$OUTDIR" ]; then
  echo "Need to specify output directory with -d"
  exit  
fi

./FScheck.sh ${CHECKARGS}

SCENARIO=Spring15v2

#### Spring15 rare backgrounds - diboson
SAMPLES=(
Spring15v2.WWToLNuQQ_13TeV-powheg \
Spring15v2.WWTo2L2Nu_13TeV-powheg \
Spring15v2.ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15v2.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15v2.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15v2.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15v2.ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15v2.WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring15v2.ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
Spring15v2.WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8 \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
