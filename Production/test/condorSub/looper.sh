#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

# run all the loopers
./looper_data.sh "$outputDir" "$KEEPTAR"
./looper_sig.sh "$outputDir" "$KEEPTAR"
./looper_qcd.sh "$outputDir" "$KEEPTAR"
./looper_ttbar.sh "$outputDir" "$KEEPTAR"
./looper_wjets.sh "$outputDir" "$KEEPTAR"
./looper_zjets.sh "$outputDir" "$KEEPTAR"
./looper_diboson.sh "$outputDir" "$KEEPTAR"
./looper_singletop.sh "$outputDir" "$KEEPTAR"
./looper_tthx.sh "$outputDir" "$KEEPTAR"
