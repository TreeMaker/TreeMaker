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
        # ttbar single lep & dilep xsecs scaled by PDG BR, assume t=tbar (hadronic: 370.78)
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 179.25, 58191090),
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 179.25, 58191090),
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 179.25, 60166355),
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 179.25, 60166355),
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 86.66, 30426583),
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 86.66, 30437492),
        MCSample("TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 2.61537118, 4964914),
        MCSample("TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 1.07722318, 3445059),
        MCSample("TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.194972521, 987054),
        MCSample("TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.0023234211, 507842),
        MCSample("WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 1635, 10142187),
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 437, 5231856),
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v3", "RunIISpring15DR74", "Constant", 59.5, 1901705),
        MCSample("WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 22.8, 1036108),
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 15.5, 3984529),
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 6.36581, 1574633),
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 1.614, 255637),
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 0.0373769, 253036),
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
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 1735000, 18717349),
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 366800, 20086103),
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 29370, 19542847),
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 6524, 15011016),
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 1064, 4963895),
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 121.5, 3848411),
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 25.42, 1961774),
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 171.46, 2625679),
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 52.58, 955972),
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 6.761, 1048047),
        MCSample("DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 2.718, 987977),
        MCSample("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 6025.2, 9052671),
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 344.9781, 5148193),
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 96.3828, 5032927),
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 13.46112, 1014139),
        MCSample("ZJetsToNuNu_HT-600ToInf_13TeV-madgraph", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 5.16969, 1015904),
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 22010, 5026005),
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 9110, 10328623),
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 273, 2476770),
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 94.5, 2550765),
        # rare backgrounds
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 3.34, 613384), # straight total = 984400
        MCSample("ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 26.23, 1695400),
        MCSample("ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 44.07, 3299800),
        MCSample("ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 35.8, 1000000),
        MCSample("ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 35.8, 995600),
        MCSample("WWTo2L2Nu_13TeV-powheg", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 12.178, 1930000),
        MCSample("ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.0122, 241254),
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.2934045, 5360227), # straight total = 18016641
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 0.2934045, 5360227), # straight total = 18016641
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9_ext2-v2", "RunIISpring15DR74", "Constant", 0.2934045, 5360227), # straight total = 18016641
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9_ext3-v1", "RunIISpring15DR74", "Constant", 0.2934045, 5360227), # straight total = 18016641
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.228, 184990), # straight total = 398000
        MCSample("TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.5297, 351398), # straight total = 749800
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.2043, 129850), # straight total = 252908
        MCSample("TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.4226, 430330), # straight total = 833964
        MCSample("ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.10035184, 1215888), # straight total = 2115118
        MCSample("WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.2595, 1240831), # straight total = 2113969
        MCSample("WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 49.997, 3212964), # straight total = 5161314
        MCSample("WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 10.71, 14344826), # straight total = 24711046
        MCSample("WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 3.058, 934728), # straight total = 1689054
        MCSample("ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 4.04, 22445861), # straight total = 36559813
        MCSample("ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 3.22, 11932246), # straight total = 18898680
        MCSample("TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.009103, 519156), # straight total = 1242940
        MCSample("TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "Asympt25ns_MCRUN2_74_V9_ext1-v1", "RunIISpring15DR74", "Constant", 0.009103, 519156), # straight total = 1242940
        MCSample("WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.1651, 221468), # straight total = 250000
        MCSample("WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.05565, 219168), # straight total = 250000
        MCSample("ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "Asympt25ns_MCRUN2_74_V9-v2", "RunIISpring15DR74", "Constant", 0.01398, 213850), # straight total = 250000
        # signal
        MCSample("SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.325388, 142674),
        MCSample("SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.0141903, 52613),
        MCSample("SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.325388, 95354),
        MCSample("SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.0252977, 49541),
        MCSample("SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.0856418, 147194),
        MCSample("SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "Asympt25ns_MCRUN2_74_V9-v1", "RunIISpring15DR74", "Constant", 0.0141903, 103140),
        # 13 TeV miniAODv2 samples - Spring15
        # backgrounds
        MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 815.96, 11344206),
        # missing: TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
        # missing: TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext1
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 179.25, 11723390),
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 179.25, 48345575),
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 86.66, 5977821),
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 86.66, 24521141),
        MCSample("TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 2.61537118, 5119009),
        MCSample("TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 1.07722318, 3510897),
        MCSample("TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.194972521, 1014678),
        MCSample("TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.0023234211, 507842),
        MCSample("WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 1635, 10152718),
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 437, 5221599),
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 59.5, 1861581),
        MCSample("WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 22.8, 1039152),
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 15.5, 4041997),
        # missing: WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 1.614, 255637),
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.0373769, 253036),
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 1735000, 18718905),
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 366800, 19905019),
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 29370, 19664159),
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 6524, 15356448),
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 1064, 4963895),
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 121.5, 3868886),
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 25.42, 1961774),
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 171.46, 2725655),
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 52.58, 973937),
        # missing: DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
        MCSample("DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 6.761, 998912),
        MCSample("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 2.718, 9042031),
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 344.9781, 5154824),
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 96.3828, 4998316),
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 13.46112, 1018882),
        # missing: ZJetsToNuNu_HT-600ToInf_13TeV-madgraph
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 22010, 5015403),
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 9110, 10424189),
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 273, 2476770),
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 94.5, 2550765),
        # rare backgrounds
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 3.34, 613384), # straight total = 984400
        # missing: ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1
        # missing: ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1
        MCSample("ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 35.8, 988500),
        MCSample("ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "74X_mcRun2_asymptotic_v2-v2", "RunIISpring15MiniAODv2", "Constant", 35.8, 995600),
        MCSample("WWTo2L2Nu_13TeV-powheg", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 12.6, 1965200),
        MCSample("ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.0122, 243654),
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.2934045, 5339546), # straight total = 17947992
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 0.2934045, 5339546), # straight total = 17947992
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2_ext2-v1", "RunIISpring15MiniAODv2", "Constant", 0.2934045, 5339546), # straight total = 17947992
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2_ext3-v1", "RunIISpring15MiniAODv2", "Constant", 0.2934045, 5339546), # straight total = 17947992
        # missing: TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8
        MCSample("TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.5297, 351398), # straight total = 749800
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.2043, 129850), # straight total = 252908
        MCSample("TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.4226, 430330), # straight total = 833964
        MCSample("ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.10035184, 1216349), # straight total = 2115877
        MCSample("WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.2595, 1278956), # straight total = 2179090
        MCSample("WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 49.997, 3134390), # straight total = 5035754
        MCSample("WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 10.71, 14346866), # straight total = 24714550
        MCSample("WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 3.058, 939034), # straight total = 1696910
        MCSample("ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 4.04, 22617684), # straight total = 36840500
        MCSample("ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 3.22, 11863244), # straight total = 18790122
        MCSample("TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.009103, 517173), # straight total = 1238145
        MCSample("TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 0.009103, 517173), # straight total = 1238145
        MCSample("WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.1651, 221468), # straight total = 250000
        MCSample("WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.05565, 219168), # straight total = 250000
        MCSample("ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.01398, 213850), # straight total = 250000
        # signal
        # all missing
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
