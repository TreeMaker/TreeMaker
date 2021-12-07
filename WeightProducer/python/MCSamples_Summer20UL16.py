import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAOD samples - Summer20UL16
Summer20UL16samples = [
    # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
    MCSample('WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 1386165),
    MCSample('WWG_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 698000, 604960),
    MCSample('WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 2900000),
    MCSample('WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4312000, 3909520), # subtotal = 62442, straight subtotal = 69000
    MCSample('WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17_ext1-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4312000, 3909520), # subtotal = 3847078, straight subtotal = 4243000
    MCSample('WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4662000, 4229098), # subtotal = 61060, straight subtotal = 67000
    MCSample('WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17_ext1-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4662000, 4229098), # subtotal = 4168038, straight subtotal = 4595000
    MCSample('WW_TuneCP5_13TeV-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 15821000),
    MCSample('WZG_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 598000, 527710),
    MCSample('WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 10441724, 6890010),
    MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4691000, 4258072), # subtotal = 124388, straight subtotal = 137000
    MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17_ext1-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4691000, 4258072), # subtotal = 4133684, straight subtotal = 4554000
    MCSample('WZ_TuneCP5_13TeV-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 7584000),
    MCSample('ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 15928000),
    MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4606000, 4103694), # subtotal = 64358, straight subtotal = 72000
    MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17_ext1-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4606000, 4103694), # subtotal = 4039336, straight subtotal = 4534000
    MCSample('ZZ_TuneCP5_13TeV-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 1151000),
    MCSample('ST_t-channel_antitop_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 29394000),
    MCSample('ST_t-channel_top_5f_InclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 55783000),
    MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 3654510),
    MCSample('tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4048000, 1095762),
    MCSample('TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 6057000, 2982392),
    MCSample('TTZToNuNu_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 1900000, 951002),
    MCSample('TTZToQQ_Dilept_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 3033000, 1526774),
    MCSample('TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 5401000, 2682510),
    MCSample('TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 3322643, 1800823),
    MCSample('TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 308983, 168951),
    MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 1416230, 504910),
    MCSample('TTGamma_Dilept_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4678000),
    MCSample('TTGamma_Hadronic_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4773000),
    MCSample('TTGamma_SingleLept_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 9654000),
    MCSample('TTWW_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 309000),
    MCSample('TTWZ_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 159000),
    MCSample('TTZZ_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 152000),
    MCSample('TTHH_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 153000),
    MCSample('TTTT_TuneCP5_13TeV-amcatnlo-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 4602000, 2011850),
    MCSample('TTWH_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 160000),
    MCSample('TTZH_TuneCP5_13TeV-madgraph-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 160000),
    MCSample('ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4941250, 1622956),
    MCSample('ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 5231575, 1719499),
    MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 19892000),
    MCSample('QCD_Pt_120to170_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 27348000),
    MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 10722000),
    MCSample('QCD_Pt_15to30_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 19298000),
    MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 29926000),
    MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 5236000),
    MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 2848000),
    MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 55264000),
    MCSample('QCD_Pt_30to50_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 19204000),
    MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 996000),
    MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 52408000),
    MCSample('QCD_Pt_50to80_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 19776000),
    MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 65088000),
    MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 37782000),
    MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 29938000),
    MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', 'FlatPU0to75_106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 9999840),
    MCSample('GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '4cores5k_106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 9624073),
    MCSample('GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 18315845),
    MCSample('ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 7083216),
    MCSample('ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 6814106),
    MCSample('ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 6114046),
    MCSample('ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 1881671),
    MCSample('ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 633500),
    MCSample('ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 115609),
    MCSample('ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 110461),
    MCSample('WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 19753958),
    MCSample('WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 15067621),
    MCSample('WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v2', 'RunIISummer20UL16MiniAODv2', 'Constant', 709514),
    MCSample('WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 2115509),
    MCSample('WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 2251807),
    MCSample('WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 19439931),
    MCSample('WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 2132228),
    MCSample('WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 82754918),
    MCSample('QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 12675816),
    MCSample('QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 73506112),
    MCSample('QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 9376965),
    MCSample('QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 4867995),
    MCSample('QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 43280518),
    MCSample('TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 43630000),
    MCSample('TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 18389000),
    MCSample('TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 18100999),
    MCSample('TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 18874000),
    MCSample('TTTo2L2Nu_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 17064000),
    MCSample('TTTo2L2Nu_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 17011000),
    MCSample('TTTo2L2Nu_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 17209000),
    MCSample('TTTo2L2Nu_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 17737000),
    MCSample('TTTo2L2Nu_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 18963000),
    MCSample('TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 144974000),
    MCSample('TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 57993000),
    MCSample('TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 60649000),
    MCSample('TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 60846000),
    MCSample('TTToSemiLeptonic_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 55105999),
    MCSample('TTToSemiLeptonic_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 62829000),
    MCSample('TTToSemiLeptonic_mtop173p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 62911000),
    MCSample('TTToSemiLeptonic_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 61416000),
    MCSample('TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 63409000),
    MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 109380000),
    MCSample('TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 41571000),
    MCSample('TTToHadronic_TuneCP5up_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 41851000),
    MCSample('TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 41728000),
    MCSample('TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 42050000),
    MCSample('TTToHadronic_mtop166p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 39944000),
    MCSample('TTToHadronic_mtop169p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 41386000),
    MCSample('TTToHadronic_mtop171p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 43046000),
    MCSample('TTToHadronic_mtop175p5_TuneCP5_13TeV-powheg-pythia8', '106X_mcRun2_asymptotic_v17-v1', 'RunIISummer20UL16MiniAODv2', 'Constant', 40447000),
]
