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
        MCSample("DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV", "PU20bx25_PHYS14_25_V1-v1", "Phys14DR", "Constant", 2.767, 4493574)
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
