import FWCore.ParameterSet.Config as cms

from TreeMaker.WeightProducer.MCSample import MCSample

# 13 TeV miniAODv2 samples - Fall17
Fall17samples = [
	# NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
	# NLO powheg 
	MCSample('TTJets_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 8026103, False, 8016963),
	# ttbar single lep & dilep xsecs scaled by PDG BR, assume t=tbar (hadronic: 377.96)
	MCSample('TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 61761347, True, 61692445),
	MCSample('TTJets_SingleLeptFromT_TuneCP2_13TeV-madgraphMLM-pythia8', 'PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1', 'RunIIFall17MiniAODv2', 'Constant', 4391055, False),
	MCSample('TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 56705550, False, 56643562),
	MCSample('TTJets_SingleLeptFromTbar_TuneCP2_13TeV-madgraphMLM-pythia8', 'PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1', 'RunIIFall17MiniAODv2', 'Constant', 4361067, False),
	MCSample('TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 28380110, False, 28349068),
	MCSample('TTJets_SingleLeptFromT_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 14368494, False, 14334094),
	MCSample('TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 8233477, False, 8213871),
	MCSample('TTJets_DiLept_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 8708805, False, 8684221),
	# HT jets: GenXSecAnalyzer scaled by ttbar inclusive k-factor (NNLO vs MCM), 831.76/502.2 = 1.6562
	MCSample('TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 81507662, False, 80817254),
	MCSample('TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 40187347, False, 39696483),
	MCSample('TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 13214871, False, 12920417),
	MCSample('TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v3', 'RunIIFall17MiniAODv2', 'Constant', 5155687, False, 4798753),
	MCSample('TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 66979742, True, 66437660),
	MCSample('TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 130725364, True, 129670780),
	MCSample('TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 111325048, True, 110424244),
        MCSample('TTToSemiLeptonic_TuneCP2_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 104362000, False, 103519416),
        MCSample('TTTo2L2Nu_TuneCP5_erdON_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5092000, False, 5050286),
        MCSample('TTToHadronic_TuneCP5_erdON_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v3', 'RunIIFall17MiniAODv2', 'Constant', 26893000, False, 26675524),
        MCSample('TTToSemiLeptonic_TuneCP5_erdON_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9117000, False, 9043828),
        MCSample('TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 3288128, True, 3273354),
        MCSample('TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 27260880, True, 27137584),
        MCSample('TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 23977012, True, 23868910),
        MCSample('TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5476459, True, 5385951),
        MCSample('TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27117982, True, 26671068),
        MCSample('TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 26849863, True, 26406444),
        MCSample('TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5500000, True, 5455706),
        MCSample('TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27108792, True, 26889896),
        MCSample('TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 20122010, True, 19959204),
        MCSample('TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5500000, True, 5455842),
        MCSample('TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 27252808, True, 27032802),
        MCSample('TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 22911672, True, 22726990),
	# WJets Inclusive
	MCSample('WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 77700506, False, 77631180), # subtotal = 33043732, straight subtotal = 33073306
	MCSample('WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 77700506, False, 77631180), # subtotal = 44587448, straight subtotal = 44627200
	# WJets HT binned: k-factor of 1.21 applied, extensions included
	MCSample('WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 35862893, False, 35804623),
	MCSample('WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 21250517, False, 21192211),
	MCSample('WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 14313274, False, 14250114),
	MCSample('WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 21709087, False, 21582309),
	MCSample('WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 20432728, False, 20272990),
	MCSample('WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 20258624, False, 19991892),
	MCSample('WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v3', 'RunIIFall17MiniAODv2', 'Constant', 21495421, False, 20629585),
        MCSample('WJetsToQQ_HT400to600_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9738307, False, 9708539),
        MCSample('WJetsToQQ_HT600to800_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 8798398, False, 8761386),
        MCSample('WJetsToQQ_HT-800toInf_qc19_3j_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 8081153, False, 8028207),
	# QCD pT-hat binned: cross sections from AN2017_013_v17, extensions included
	MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 56387936, False), # subtotal = 28430936
	MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 56387936, False), # subtotal = 27957000
	MCSample('QCD_Pt_120to170_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 29854280, False),
	MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 56298920, True), # subtotal = 29829920
	MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 56298920, True), # subtotal = 26469000
	MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 111229780, True), # subtotal = 53798780
	MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v3', 'RunIIFall17MiniAODv2', 'Constant', 111229780, True), # subtotal = 57431000
	MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 55503028, False), # subtotal = 27881028
	MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v3', 'RunIIFall17MiniAODv2', 'Constant', 55503028, False), # subtotal = 27622000
	MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 128548964, True), # subtotal = 66134964
	MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 128548964, True), # subtotal = 62414000
	MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 78116008, False), # subtotal = 39529008
	MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 78116008, False), # subtotal = 38587000
	MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 35819814, True), # subtotal = 16188000
	MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 35819814, True), # subtotal = 19631814
	MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 11353270, True), # subtotal = 5685270
	MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v3', 'RunIIFall17MiniAODv2', 'Constant', 11353270, True), # subtotal = 5668000
	MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 2923941, True),
	MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 1910526, True),
	MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 956837, False), # subtotal = 757837
	MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 956837, False), # subtotal = 199000
	MCSample('QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5859904, True),
	MCSample('QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 28213684, True),
	MCSample('QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 29030324, True),
	MCSample('QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 24068613, True),
	MCSample('QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 23248995, True),
	MCSample('QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 20774848, True),
	MCSample('QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 46170668, True),
	MCSample('QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 17744779, False),
	MCSample('QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 24243589, True),
        MCSample('QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 17263676, False),
        MCSample('QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 17114527, False),
        MCSample('QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 11596693, False),
	# QCD: extensions included
	MCSample('QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 59026308, False, 58959570), # without missing files = 59427619
	MCSample('QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 21127542, False, 21088604),
	MCSample('QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 56207744, False, 56041018),
	MCSample('QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 20029078, False, 19942498), # without missing files = 20006396
	MCSample('QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 16882838, False, 16770762),
	MCSample('QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 11634434, False, 11508604),
	MCSample('QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 5941306, False, 5825566),
	# DY/Z: k-factor of 1.23 applied, available extensions included
	MCSample('DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 14185757, True, 14163583), # subtotal = 10219538, straight subtotal = 10235418
	MCSample('DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 14185757, True, 14163583), # subtotal = 3944045, straight subtotal = 3950339
	MCSample('DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 11499275, True, 11467829), # subtotal = 10270122, straight subtotal = 10298412
	MCSample('DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 11499275, True, 11467829), # subtotal = 1197707, straight subtotal = 1200863
	MCSample('DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 10657929, True, 10611153), # subtotal = 9491947, straight subtotal = 9533635
	MCSample('DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 10657929, True, 10611153), # subtotal = 1119206, straight subtotal = 1124294
	MCSample('DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 8153358, True, 8104916),
	MCSample('DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 3089861, True, 3064779),
	MCSample('DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 625517, True, 616923),
	MCSample('DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 404986, True, 387646),
	MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 97800939, True, 97714787), # subtotal = 48632630, straight subtotal = 48675378
	MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 97800939, True, 97714787), # subtotal = 49082157, straight subtotal = 49125561
	MCSample('ZJetsToNuNu_HT-100To200_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 22737266, True, 22702468),
	MCSample('ZJetsToNuNu_HT-200To400_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 21675916, True, 21618510),
	MCSample('ZJetsToNuNu_HT-400To600_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9134120, True, 9094890),
	MCSample('ZJetsToNuNu_HT-600To800_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5697594, True, 5664642),
	MCSample('ZJetsToNuNu_HT-800To1200_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 2058077, True, 2041779),
	MCSample('ZJetsToNuNu_HT-1200To2500_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 338948, True, 334332),
	MCSample('ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 6734, True, 6446),
	MCSample('GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9959190, True, 9957110),
	MCSample('GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 18536907, True, 18524305),
	MCSample('GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4646958, False, 4640128),
	MCSample('GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 3289629, False, 3278039),
	MCSample('GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8_v2', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 15965137, False, 15961733),
	MCSample('GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_v2', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 49904818, False, 49868596), #DAS has 49928037 events, but was reduced because one file was corrupt
	MCSample('GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_v2', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 13389304, False, 13367286),
	MCSample('GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 8392881, False, 8361249),
	# single top: NoFullyHadronicDecays xsec scaled by BF for non-fully-hadronic (1-(1-3*0.108)^2
	MCSample('ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9568575, True, 5970607),
	MCSample('ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9906720, True, 6179792),
        MCSample('ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9652000, False, 6018732),
	MCSample('ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5865875, True),
	MCSample('ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 3939990, True),
	MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 11502515, True, 8399349), # subtotal = 5334538, straight subtotal = 5375230
	MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 11502515, True, 8399349), # subtotal = 3064811, straight subtotal = 6127285
	MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5389364, True, 5347818),
	MCSample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4974435, True, 4936387),
	MCSample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4703458, True, 4666898),
	MCSample('ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 7780870, True, 7721566),
	MCSample('ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 7993682, True, 7932626),
	MCSample('ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 7581624, True, 7523294),
	MCSample('ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 7660001, True, 7601399),        
	MCSample('tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 1000000, False, 262096),
	# rare backgrounds:
	MCSample('WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 4121843, False, 4110545),
	MCSample('WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5054286, True, 3169582),
	MCSample('WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 19086373, False, 11347099),
	MCSample('WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4994395, False, 2717911),
	MCSample('ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27840918, False, 17768294),
	MCSample('ZZTo2L2Nu_13TeV_powheg_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 8744768, False, 8733658),
	MCSample('ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 62172314, False, 39238220),
	MCSample('TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 7563490, True, 3570720),
	MCSample('TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 750000, True, 356286),
	MCSample('TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4925829, True, 2678775),
	MCSample('TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4849525, True, 2654107),# total (DAS) = 4919674, total (after failures) = 4849525
	MCSample('TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 811306, True, 441560),
	MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 14026117, True, 5441639), # subtotal = 1795589, straight subtotal = 4623345
	MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 14026117, True, 5441639), # subtotal = 3646050, straight subtotal = 9402772
	MCSample('ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9659185, True, 3324103),
	MCSample('ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9911561, True, 3409351),
	MCSample('TTGamma_SingleLeptFromT_TuneCP5_PSweights_13TeV_madgraph_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4911716, False, 4910406),
	MCSample('TTGamma_SingleLeptFromTbar_TuneCP5_PSweights_13TeV_madgraph_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4809392, False, 4807960),
	MCSample('TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4642344, False, 4641882),
	MCSample('TTTT_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_pilot_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 993804, True, 371504),
	MCSample('TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 2273928, False, 849964),
	MCSample('TTHH_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 199374),
	MCSample('TTTW_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 199704),
	MCSample('TTWH_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 198982),
	MCSample('TTWW_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, False, 199010),
	MCSample('TTWZ_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 198758),
	MCSample('TTZH_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 199286),
	MCSample('TTZZ_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 199372),
	MCSample('TTTJ_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 200000, False, 198546),
	MCSample('WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 232300, False, 203246),
	MCSample('WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 250000, False, 219964),
	MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 250000, True, 219660),
	MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 250000, True, 213514),
        MCSample('WZ_TuneCP5_13TeV-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 3928630, True),
        MCSample('WW_TuneCP5_13TeV-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 7765828, True),
        MCSample('ZZ_TuneCP5_13TeV-pythia8', 'PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 1925931, True),
	# signal
	MCSample('SMS-T1tttt_mGluino-1200_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 147547, False),
	MCSample('SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 51480, False),
	MCSample('SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 100612, False),
	MCSample('SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 50457, False),
	MCSample('SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 154683, False),
	MCSample('SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 47088, False),
	MCSample('SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 91673, False),
	MCSample('SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 99440, False, 98520),
	MCSample('SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 222410, False),
	MCSample('SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 248828, False, 243114),
	MCSample('SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 202760, False),
	MCSample('SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 250392, False, 231034),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-175_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 986787, False, 985875),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-50_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 988301, False, 986921),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-75_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 987809, False, 986339),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-250_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 985567, False, 984057),
        MCSample('SMS-T2tt_3J_xqcut-20_mStop-700_mLSP-525_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 922555, False, 911187),
	# stealth/rpv stop signals
        MCSample('RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 1023815, False), # subtotal = 511693
        MCSample('RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 1023815, False), # subtotal = 512122
	MCSample('RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 533878, False, 532748),
        MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 1017889, False), # subtotal = 507649
        MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 1017889, False), # subtotal = 510240
	MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 523220, False, 521846),
        MCSample('RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 965261, False), # subtotal = 460837
        MCSample('RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 965261, False), # subtotal = 504424
	MCSample('RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 553126, False, 551420),
        MCSample('RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 763924, False), # subtotal = 381796
        MCSample('RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 763924, False), # subtotal = 382128
	MCSample('RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 388250, False, 386558),
        MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 421716, False), # subtotal = 210725
        MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 421716, False), # subtotal = 210991
	MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 220618, False, 219422),
        MCSample('RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 247285, False), # subtotal = 123462
        MCSample('RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 247285, False), # subtotal = 123823
	MCSample('RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 126676, False, 125906),
        MCSample('RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 146896, False), # subtotal = 73189
        MCSample('RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 146896, False), # subtotal = 73707
	MCSample('RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 79816, False, 79158),
        MCSample('RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 103572, False), # subtotal = 51755
        MCSample('RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 103572, False), # subtotal = 51817
	MCSample('RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 56056, False, 55514),
        MCSample('RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 102108, False), # subtotal = 51218
        MCSample('RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 102108, False), # subtotal = 50890
	MCSample('RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 51093, False, 50499),
        MCSample('RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 101839, False), # subtotal = 50807
        MCSample('RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 101839, False), # subtotal = 51032
	MCSample('RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 52800, False, 51998),
        MCSample('RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 52299, False), # subtotal = 26030
        MCSample('RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 52299, False), # subtotal = 26269
	MCSample('RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27606, False, 27104),
        MCSample('RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 52831, False), # subtotal = 26545
        MCSample('RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 52831, False), # subtotal = 26286
	MCSample('RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27810, False, 27156),
        MCSample('RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 55207, False), # subtotal = 27490
        MCSample('RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 55207, False), # subtotal = 27717
	MCSample('RPV_2t6j_mStop-900_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 29186, False, 28344),
	MCSample('StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 532773, False, 531723),
	MCSample('StealthSYY_2t6j_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 527458, False, 526108),
	MCSample('StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 552139, False, 550291),
	MCSample('StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 429082, False, 427160),
	MCSample('StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 215579, False, 214375),
	MCSample('StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 138221, False, 137309),
	MCSample('StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 81907, False, 81181),
	MCSample('StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 54610, False, 53986),
	MCSample('StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v3', 'RunIIFall17MiniAODv2', 'Constant', 47985, False, 47381),
	MCSample('StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 52468, False, 51664),
	MCSample('StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 28401, False, 27875),
	MCSample('StealthSYY_2t6j_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 28919, False, 28333),
	MCSample('StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 29807, False, 29057),
	MCSample('StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 573000, False, 571908),
	MCSample('StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 566558, False, 565120),
	MCSample('StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 566202, False, 564294),
	MCSample('StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 427664, False, 425820),
	MCSample('StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 211657, False, 210577),
	MCSample('StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 137385, False, 136455),
	MCSample('StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 81875, False, 81161),
	MCSample('StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 57823, False, 57277),
	MCSample('StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 56198, False, 55594),
	MCSample('StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 56036, False, 55196),
	MCSample('StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 28446, False, 27928),
	MCSample('StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 28880, False, 28256),
]
