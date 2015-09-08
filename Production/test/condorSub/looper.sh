#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### squark
#python generateSubmission.py -o $outputDir -c Phys14 -n 1 -s -f PHYS14.SMS-T2bb_2J_mStop-600_mLSP-580_Tune4C_13TeV-madgraph-tauola
#python generateSubmission.py -o $outputDir -c Phys14 -n 1 -s -f PHYS14.SMS-T2bb_2J_mStop-900_mLSP-100_Tune4C_13TeV-madgraph-tauola
#python generateSubmission.py -o $outputDir -c Phys14 -n 1 -s -f PHYS14.SMS-T2qq_2J_mStop-1200_mLSP-100_Tune4C_13TeV-madgraph-tauola
#python generateSubmission.py -o $outputDir -c Phys14 -n 1 -s -f PHYS14.SMS-T2qq_2J_mStop-600_mLSP-550_Tune4C_13TeV-madgraph-tauola

#### Run2015B Prompt RECO
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.DoubleEG 
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.DoubleMuon 
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.HTMHT 
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.SingleElectron 
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.SingleMuon 
python generateSubmission.py -n 1 -s -o $outputDir -c 2015B -f Run2015B-PromptReco-v1.SinglePhoton

#### Run2015B July 17 reprocessing
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.DoubleEG
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.DoubleMuon
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.EGamma
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.HTMHT
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.SingleElectron
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.SingleMu
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.SingleMuon
python generateSubmission.py -n 1 -s  -o $outputDir -c re2015B -f Run2015B-17Jul2015-v1.SinglePhoton

#### Spring15 backgrounds
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZJetsToNuNu_HT-200To400_13TeV-madgraph
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZJetsToNuNu_HT-400To600_13TeV-madgraph
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ZJetsToNuNu_HT-600ToInf_13TeV-madgraph
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8

#### Spring15 rare backgrounds
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WWToLNuQQ_13TeV-powheg
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.WWTo2L2Nu_13TeV-powheg
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1

#### Spring15 gluino
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8

