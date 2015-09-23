#!/bin/bash

if [ "$1" == 1 ]; then 
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

# run all the loopers
./looper_data.sh "$OUTPUTDIR" "$KEEPTAR"
./looper_sig.sh "$OUTPUTDIR" "$KEEPTAR"
./looper_qcd.sh "$OUTPUTDIR" "$KEEPTAR"
./looper_ttbar.sh "$OUTPUTDIR" "$KEEPTAR"
./looper_wjets.sh "$OUTPUTDIR" "$KEEPTAR"
./looper_zjets.sh "$OUTPUTDIR" "$KEEPTAR"
./looper_diboson.sh "$OUTPUTDIR" "$KEEPTAR"
./looper_singletop.sh "$OUTPUTDIR" "$KEEPTAR"
./looper_tthx.sh "$OUTPUTDIR" "$KEEPTAR"
