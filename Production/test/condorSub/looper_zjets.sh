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

#### Spring16 backgrounds - zjets
SAMPLES=(
Spring16.DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1 \
Spring16.ZJetsToNuNu_HT-100To200_13TeV-madgraph_ext1 \
Spring16.ZJetsToNuNu_HT-200To400_13TeV-madgraph_ext1 \
Spring16.ZJetsToNuNu_HT-600To800_13TeV-madgraph \
Spring16.ZJetsToNuNu_HT-800To1200_13TeV-madgraph \
Spring16.ZJetsToNuNu_HT-1200To2500_13TeV-madgraph \
Spring16.ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph \
Spring16.GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring16.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
)

#missing:
#Spring16.DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
#Spring16.ZJetsToNuNu_HT-400To600_13TeV-madgraph \

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
