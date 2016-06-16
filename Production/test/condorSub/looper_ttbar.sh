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

#### Spring16 backgrounds - ttbar
SAMPLES=(
Spring16.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
)

#missing:
#Spring16.TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
