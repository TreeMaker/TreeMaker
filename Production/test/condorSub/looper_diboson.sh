#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15

#### Spring15 rare backgrounds - diboson
SAMPLES="
Spring15.WWToLNuQQ_13TeV-powheg \
Spring15.WWTo2L2Nu_13TeV-powheg \
Spring15.ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15.WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15.WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15.WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8 \
Spring15.ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8
"

for SAMPLE in ${SAMPLES}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
