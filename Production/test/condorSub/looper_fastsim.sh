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

SCENARIO=Spring16Fastsig

#### Spring16 gluino - fastsim scans
SAMPLES=(
Spring16Fast.SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16Fast.SMS-T2bb_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16Fast.SMS-T2tt_mStop-400to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16Fast.SMS-T2tt_mStop-350to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16Fast.SMS-T2tt_mStop-250to350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16Fast.SMS-T1bbbb_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
)

# missing: lots

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
