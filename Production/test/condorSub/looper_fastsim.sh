#!/bin/bash

if [ "$1" == 1 ]; then
  echo "Need to specify output directory in argument 1"
  exit
fi

OUTPUTDIR=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

SCENARIO=Spring15Fastv2

#### Spring15 gluino - fastsim scans
SAMPLES=(
Spring15Fastv2.SMS-T1bbbb_mGlu-1025-1050_mLSP-800to975-400to800-1000to1025_TuneCUETP8M1_13TeV-madgraph-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGlu-1050-1075_mLSP-850to975-850to925-1000to1050_TuneCUETP8M1_13TeV-madgraph-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGlu-1250-1275_mLSP-400to950-1175to1200-1050to1175_TuneCUETP8M1_13TeV-madgraph-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1000-1025_mLSP-1to975-1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1075_mLSP-950to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1100_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1125-1150_mLSP-900to1100-1000to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1150_mLSP-400to975-1100to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1175_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1200_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1225-1250_mLSP-1000to1175-1000to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1300_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1325-1350_mLSP-1100to1175-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1350-1375_mLSP-1to950-1150to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1400-1450_mLSP-1to1350-1to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1500-1550_mLSP-1to1300-1000to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1550_mLSP-1to950-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1650-1700_mLSP-350to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1700-1750_mLSP-700to1450-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1750_mLSP-700to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1800-1850_mLSP-1to1450-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1850-1900_mLSP-500to1450-1to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-1900-1950_mLSP-1000to1450-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-2000_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-625_mLSP-400to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-650_mLSP-475to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-675_mLSP-450to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-700-725-750_mLSP-625to675-500to700-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-700_mLSP-1to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-750-775_mLSP-400to725-550to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-775_mLSP-625to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-800-825_mLSP-1to775-600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-825-850_mLSP-625to800-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-850-875_mLSP-725to825-650to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-925-950_mLSP-725to900-400to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-950-975_mLSP-825to925-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1000to1025_mLSP-1to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1025to1075_mLSP-400to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1075_mLSP-925to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1100to1125_mLSP-1to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1125to1175_mLSP-925to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1225to1250_mLSP-1to1225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1250to1275_mLSP-550to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1300to1325_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1325to1350_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1350to1375_mLSP-650to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1400to1450_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1450to1500_mLSP-1to1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1500to1550_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1550_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1600to1650_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1650to1750_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1750_mLSP-50to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1800to1850_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1850to1950_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1950to2000_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-2000_mLSP-50to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-600_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-600_mLSP-400to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-625_mLSP-425to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-625to650_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-675_mLSP-500to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-750to775_mLSP-450to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-800to825_mLSP-1to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-925to975_mLSP-400to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-650to675_mLSP-475to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-700_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-700to750_mLSP-400to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1qqqq_mGluino-925to975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1000to1050_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1100_mLSP-1to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1100to1125_mLSP-700to900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1150_mLSP-1to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1150to1175_mLSP-750to925_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1175_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1250to1275_mLSP-700to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1300_mLSP-1to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1300to1325_mLSP-700to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1350to1375_mLSP-50to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1400_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1400to1425_mLSP-50to1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1425to1450_mLSP-1to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1475to1500_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1500to1525_mLSP-50to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1525to1550_mLSP-1to1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1600to1650_mLSP-1to1350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1650to1700_mLSP-1to1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1700to1750_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1800to1850_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1850to1900_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1950_mLSP-700to950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-625_mLSP-275to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-625to650_mLSP-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-650to675_mLSP-250to425_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-675_mLSP-325to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-700to750_mLSP-200to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-800to825_mLSP-1to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-825to850_mLSP-200to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-875to900_mLSP-1to650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-950to975_mLSP-350to725_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1000_mLSP-1to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-600_mLSP-250to325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-600to625_mLSP-250to375_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-600_mLSP-1to225_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1550to1575_mLSP-500to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1050_mLSP-50to775_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1050to1075_mLSP-650to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-1225to1250_mLSP-1to1025_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T1tttt_mGluino-900to950_mLSP-200to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-1000To1075_mLSP-1To950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-1100To1175_mLSP-1to1050_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-1200To1275_mLSP-1to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-1300To1375_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-1400To1550_mLSP-1To1275_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-1600To1750_mLSP-1To950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-1800to2000_mLSP-1to1250_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-600To675_mLSP-1to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-700To775_mLSP-1To650_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T5qqqqVV_mGluino-800To975_mLSP-1To850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-100-125_mLSP-1to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-150-175_mLSP-1to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-200_mLSP-1to125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-225_mLSP-25to150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-250_mLSP-1to175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-300to375_mLSP-1to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-275_mLSP-75to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-400to475_mLSP-1to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-500-525-550_mLSP-1to425-325to450-1to475_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
Spring15Fastv2.SMS-T2tt_mStop-600-950_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 \
)

for SAMPLE in ${SAMPLES[@]}; do
  python generateSubmission.py -n 1 -s -o ${OUTPUTDIR} -c ${SCENARIO} -f ${SAMPLE}
done
