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

# run all the loopers
./looper_data.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_sig.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_qcd.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_ttbar.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_wjets.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_zjets.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_diboson.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_singletop.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_tthx.sh -d "$OUTPUTDIR" "$CHECKARGS"
#./looper_74X.sh -d "$OUTPUTDIR" "$CHECKARGS"
./looper_fastsim.sh -d "$OUTPUTDIR" "$CHECKARGS"
#./looper_priv.sh -d "$OUTPUTDIR" "$CHECKARGS"
