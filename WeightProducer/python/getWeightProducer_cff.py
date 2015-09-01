# $Id: getWeightProducer_cff.py,v 1.7 2012/11/05 14:58:14 mschrode Exp $
#
# Returns a WeightProducer module that knows at runtime
# which data sample is produced and thus, what weights
# are required. The function can be used as follows:
#
#    from RA2Classic.WeightProducer.getWeightProducer_cff import getWeightProducer
#    process.WeightProducer = getWeightProducer(process.source.fileNames[0])

import FWCore.ParameterSet.Config as cms

class MCSample:
    def __init__(self, name, production, mcVersion, Method, XS, NumberEvts):
        self.name = name
        self.production = production
        self.mcVersion = mcVersion
        self.Method = Method
        self.XS = XS
        self.NumberEvts = NumberEvts

def getWeightProducer(fileName):

    mcVersion = "none"                  # For lumi and PU weights
    applyWeight = False
    
    ## --- Setup default WeightProducer ------------------------------------
    
    # Import weightProducer
    from TreeMaker.WeightProducer.weightProducer_cfi import weightProducer
    
    # Set default values to produce an event weight of 1
    weightProducer.weight = cms.double(1.0)
    weightProducer.Method = cms.string("Constant")
    weightProducer.LumiScale = cms.double(1.0)
    weightProducer.FileNamePUDataDistribution = cms.string("NONE")
    weightProducer.PU = cms.int32(0)

    # list of samples
    samples = [
        # 13 TeV miniAOD samples - CSA14
        # backgrounds
        MCSample("TTJets_MSDecaysCKM_central_Tune4C_13TeV", "PU40bx25_POSTLS170_V5-v2", "Spring14miniaod", "Constant", 745.16, 25478151),
        MCSample("TTJets_MSDecaysCKM_central_Tune4C_13TeV", "PU20bx25_POSTLS170_V5-v2", "Spring14miniaod", "Constant", 818.8, 25474122),
        MCSample("WJetsToLNu_HT-100to200_Tune4C_13TeV", "PU20bx25_POSTLS170_V5-v2", "Spring14miniaod", "Constant", 2235.0, 5229141),
        MCSample("WJetsToLNu_HT-200to400_Tune4C_13TeV", "PU20bx25_POSTLS170_V5-v1", "Spring14miniaod", "Constant", 580.1, 4933933),
        MCSample("WJetsToLNu_HT-400to600_Tune4C_13TeV", "PU20bx25_POSTLS170_V5-v1", "Spring14miniaod", "Constant", 68.40, 4642823),
        MCSample("WJetsToLNu_HT-600toInf_Tune4C_13TeV", "PU20bx25_POSTLS170_V5-v1", "Spring14miniaod", "Constant", 23.14, 4634811),
        MCSample("QCD_Pt-470to600_Tune4C_13TeV_pythia8", "PU20bx25_POSTLS170_V5-v1", "Spring14miniaod", "Constant", 587.1, 2907137),
        #signal
        MCSample("SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola", "PU_S14_POSTLS170_V6AN1", "Spring14dr", "Constant", 0.0856418, 100322),
        MCSample("SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola", "PU_S14_POSTLS170_V6AN1", "Spring14dr", "Constant", 0.0141903, 105679),
        MCSample("SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola", "PU_S14_POSTLS170_V6AN1", "Spring14dr", "Constant", 0.325388, 97584),
        MCSample("SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola", "PU_S14_POSTLS170_V6AN1", "Spring14dr", "Constant", 0.0141903, 105964),
        MCSample("SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola", "PU_S14_POSTLS170_V6AN1", "Spring14dr", "Constant", 0.325388, 97513),
        MCSample("SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola", "PU_S14_POSTLS170_V6AN1", "Spring14dr", "Constant", 0.0252977, 103943),
        MCSample("TTJets_MSDecaysCKM_central_Tune4C_13TeV", "PU40bx25_POSTLS170_V5-v2", "Spring14miniaod", "Constant", 745.16, 25478151),
        # 13 TeV miniAOD samples - PHYS14
        # signal
        MCSample("SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola", "PU20bx25_tsg_PHYS14", "Phys14DR", "Constant",  0.0252977 , 102891),
        MCSample("SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola", "PU20bx25_tsg_PHYS14", "Phys14DR", "Constant",  0.325388 , 96681),
        MCSample("SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola", "PU20bx25_tsg_PHYS14", "Phys14DR", "Constant", 0.325388, 97584),
        MCSample("SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola", "PU20bx25_tsg_PHYS14", "Phys14DR", "Constant", 0.0141903, 105964),
        MCSample("SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola", "PU20bx25_tsg_PHYS14", "Phys14DR", "Constant", 0.0856418, 100322),
        MCSample("SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola", "PU20bx25_tsg_PHYS14", "Phys14DR", "Constant", 0.0141903, 105679),
        # backgrounds
        # QCD MG
        MCSample("QCD_HT_250To500_13TeV-madgraph", "PU20bx25_PHYS14_25_V1", "Phys14DR", "Constant", 6.705e+5, 2668172),
        MCSample("QCD_HT-500To1000_13TeV-madgraph", "PU20bx25_PHYS14_25_V1", "Phys14DR", "Constant", 2.674e+4, 4063345),
        MCSample("QCD_HT_1000ToInf_13TeV-madgraph", "PU20bx25_PHYS14_25_V1", "Phys14DR", "Constant", 769.7, 1464453),
        # QCD Pythia
        MCSample("QCD_Pt-15to30_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 1837410000, 1986539),
        MCSample("QCD_Pt-30to50_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 161500000, 1988880),
        MCSample("QCD_Pt-50to80_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 22110000, 2000338),
        MCSample("QCD_Pt-80to120_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 3000114, 2000340),
        MCSample("QCD_Pt-120to170_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 493200, 2001453),
        MCSample("QCD_Pt-170to300_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 120300, 2000704),
        MCSample("QCD_Pt-300to470_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 7475, 1986177),
        MCSample("QCD_Pt-470to600_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 587.1, 2001071),
        MCSample("QCD_Pt-600to800_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 167, 1997744),
        MCSample("QCD_Pt-800to1000_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 28.25, 1000065),
        MCSample("QCD_Pt-1000to1400_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 8.195, 500550),
        MCSample("QCD_Pt-1400to1800_Tune4C_13TeV", "PU20bx25_trkalmb_castor_PHYS14_25_V1", "Phys14DR", "Constant", 0.7346, 199627),
        MCSample("QCD_Pt-1800to2400_Tune4C_13TeV", "PU20bx25_trkalmb_PHYS14_25_V1", "Phys14DR", "Constant", 0.102, 200079),
        MCSample("QCD_Pt-2400to3200_Tune4C_13TeV", "PU20bx25_trkalmb_PHYS14_25_V1", "Phys14DR", "Constant", 0.0064, 200453),
        MCSample("QCD_Pt-3200_Tune4C_13TeV", "PU20bx25_trkalmb_PHYS14_25_V1", "Phys14DR", "Constant", 0.000163, 200200),
        MCSample("TBarToLeptons_t-channel_Tune4C_CSA14_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 61.6, 1999800),
        MCSample("TBarToLeptons_s-channel-CSA14_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 1.0, 250000),
        MCSample("TToLeptons_t-channel-CSA14_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 103.4, 3991000),
        MCSample("TToLeptons_s-channel-CSA14_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 2.0, 500000),
        MCSample("TTZJets_Tune4C_13TeV-madgraph-tauola", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 2.232, 249275),
        MCSample("TTWJets_Tune4C_13TeV-madgraph-tauola", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 1.152, 246521),
        MCSample("T_tW-channel-DR_Tune4C_13TeV-CSA14", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 35.0, 986100),
        MCSample("TTJets_MSDecaysCKM_central_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 806.1, 25446993),
        MCSample("WJetsToLNu_HT-100to200_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 2235.0, 5262265),
        MCSample("WJetsToLNu_HT-200to400_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 580.1, 4936077),
        MCSample("WJetsToLNu_HT-400to600_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 68.40, 4640594),
        MCSample("WJetsToLNu_HT-600toInf_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 23.14, 4581841),
        MCSample("ZJetsToNuNu_HT-100to200_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 473.2, 4986424),
        MCSample("ZJetsToNuNu_HT-200to400_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 128.0, 4546470),
        MCSample("ZJetsToNuNu_HT-400to600_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v2", "Phys14DR", "Constant", 15.23, 4433784),
        MCSample("ZJetsToNuNu_HT-600toInf_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 5.224, 4463806),
        MCSample("DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 246.8, 4054159),
        MCSample("DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 66.34, 4666496),
        MCSample("DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 8.313, 4931372),
        MCSample("DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 2.767, 4493574),
        MCSample("GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 1534, 4734234),
        MCSample("GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 489.9, 4533420),
        MCSample("GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 62.05, 4560801),
        MCSample("GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 20.87, 4341179),        
        # 13 TeV miniAOD samples - Spring15
        # backgrounds
        # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
        MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 815.96, 11339232),
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 186, 58191090),
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 186, 58191090),
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 186.2, 60166355),
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 186.2, 60166355),
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 93.18, 30437492),
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 93.18, 30437492),
        MCSample("TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 2.61537118, 4964914),
        MCSample("TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 1.07722318, 3445059),
        MCSample("TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.194972521, 987054),
        MCSample("TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.0023234211, 507842),
        MCSample("WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 1635, 10142187),
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 437, 5231856),
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v3", "RunIISpring15DR74", "Constant", 59.5, 1901705),
        MCSample("WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 22.8, 1036108),
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 3.34, 613384), # straight total = 984400
        MCSample("ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 26.23, 1695400),
        MCSample("ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 44.07, 3299800),
        MCSample("ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 35.8, 1000000),
        MCSample("ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 35.8, 995600),
        MCSample("WWTo2L2Nu_13TeV-powheg", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 12.6, 1930000),
        MCSample("WWToLNuQQ_13TeV-powheg", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 52.2, 1969600),
        MCSample("ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.0122, 241254),
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.290, 482322), # straight total = 1612604
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 0.290, 770921), # straigh total = 2588639
        MCSample("QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 2762530, 3424782),
        MCSample("QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 471100, 3452896),
        MCSample("QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 117276, 3364368),
        MCSample("QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 7823, 2933611),
        MCSample("QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 648.2, 1936832),
        MCSample("QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v3", "RunIISpring15DR74", "Constant", 186.9, 1964128),
        MCSample("QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 32.293, 1937216),
        MCSample("QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 9.4183, 1487136),
        MCSample("QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.84265, 197959),
        MCSample("QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.114943, 193608),
        MCSample("QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.00682981, 194456),
        MCSample("QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.000165445, 192944),
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 171.46, 2625679),
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 52.58, 955972),
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 6.761, 1048047),
        MCSample("DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 2.718, 987977),
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 78.36, 5032927),
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 10.944, 1014139),
        MCSample("ZJetsToNuNu_HT-600ToInf_13TeV-madgraph", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 4.203, 1015904),
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 1534, 5026005),
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 489.9, 10328623),
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 62.05, 2476770),
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 20.87, 2550765),
    ]
    
    # loop over all samples until we find a match
    for sample in samples:
        if sample.name in fileName and sample.production in fileName:
            mcVersion = sample.mcVersion
            weightProducer.Method     = cms.string(sample.Method)
            weightProducer.XS         = cms.double(sample.XS)
            weightProducer.NumberEvts = cms.double(sample.NumberEvts)
            print sample.name+", "+sample.production+" : '"+fileName+"'"
            applyWeight = True
            weightProducer.weight = cms.double(-1.)
            break

    ## --- PU Reweighting and Lumi ------------------------------------------------

    if mcVersion == "Summer12_5_3_X":
        weightProducer.weight = cms.double(-1.)
        weightProducer.Lumi = cms.double(19466)
        weightProducer.PU = cms.int32(3) # PU S10
        weightProducer.FileNamePUDataDistribution = cms.string("RA2Classic/WeightProducer/data/DataPileupHistogram_RA2Summer12_190456-208686_ABCD.root")
        applyWeight = True
	
    if applyWeight:
        print "Setup WeightProducer for '"+fileName+"'"

    return weightProducer
