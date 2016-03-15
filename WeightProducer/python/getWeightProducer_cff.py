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
        # 13 TeV miniAODv2 samples - Spring15
        # backgrounds
        # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
        MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 831.76, 11344206),
        # ttbar single lep & dilep xsecs scaled by PDG BR, assume t=tbar (hadronic: 377.96)
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 182.72, 60186393),
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 182.72, 60186393),
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 182.72, 59816364),
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 182.72, 59816364),
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 88.34, 30498962),
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 88.34, 30498962),
        # HT jets: MCM scaled by ttbar inclusive k-factor (NNLO vs MCM), 831.76/502.2 = 1.656
        MCSample("TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant",   2.678835503, 5119009),
        MCSample("TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant",  1.103362965, 3510897),
        MCSample("TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.199703704, 1014678),
        MCSample("TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant",  0.002379801, 507842),
        # WJets: k-factor of 1.21 applied
        MCSample("WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 1627.45, 10152718),
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 435.24, 5221599),
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 59.18, 1745914),
        MCSample("WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 22.71, 1039152),
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 14.58, 4041997),
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 6.66, 1574633),
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 1.608, 255637),
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.03891, 253036),
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant",   1717000, 18718905),
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant",   351300, 19826197),
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant",   31630, 19664159),
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant",  6802, 15356448),
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 1206, 4963895),
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 120.4, 3868886),
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant",  25.24, 1912529),
        # DY/Z: k-factor of 1.23 applied
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 183.1, 11079482), # subtotal = 2725655
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 183.1, 11079482), # subtotal = 8353827
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 50.49, 9580541), # subtotal = 973937
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 50.49, 9580541), # subtotal = 8606604
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v2", "RunIISpring15MiniAODv2", "Constant", 6.994, 10420186), # subtotal = 1067758
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 6.994, 10420186), # subtotal = 9352428
        MCSample("DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 2.700, 4902520), # subtotal = 998912
        MCSample("DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 2.700, 4902520), # subtotal = 3903608
        MCSample("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 6025.2, 9042031),
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 344.3, 5154824),
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 95.23, 4998316),
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 13.19, 1018882),
        MCSample("ZJetsToNuNu_HT-600ToInf_13TeV-madgraph", "74X_mcRun2_asymptotic_v2-v2", "RunIISpring15MiniAODv2", "Constant", 5.063, 1008333),
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 9226, 5015403),
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 2300, 10424189),
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 277.4, 2476770),
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 93.38, 2550765),
        # rare backgrounds
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 3.34, 613384), # straight total = 984400
        MCSample("ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 26.23, 1680200),
        MCSample("ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 44.07, 3299800),
        MCSample("ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 35.6, 988500),
        MCSample("ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "74X_mcRun2_asymptotic_v2-v2", "RunIISpring15MiniAODv2", "Constant", 35.6, 995600),
        MCSample("WWTo2L2Nu_13TeV-powheg", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 12.178, 1965200),
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.2934045, 5339546), # straight total = 17947992
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2_ext1-v1", "RunIISpring15MiniAODv2", "Constant", 0.2934045, 5339546), # straight total = 17947992
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2_ext2-v1", "RunIISpring15MiniAODv2", "Constant", 0.2934045, 5339546), # straight total = 17947992
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "74X_mcRun2_asymptotic_v2_ext3-v1", "RunIISpring15MiniAODv2", "Constant", 0.2934045, 5339546), # straight total = 17947992
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "74X_mcRun2_asymptotic_v2-v2", "RunIISpring15MiniAODv2", "Constant", 0.2529, 184990), # straight total = 398000
        MCSample("TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.5297, 351398), # straight total = 749800
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.2043, 129850), # straight total = 252908
        MCSample("TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.4026, 430330), # straight total = 833964
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
        MCSample("SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.325388, 142674),
        MCSample("SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.0141903, 52613),
        MCSample("SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.325388, 95354),
        MCSample("SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.0252977, 49541),
        MCSample("SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.0856418, 147194),
        MCSample("SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.0141903, 103140),
        MCSample("SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.51848, 388207),
        MCSample("SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "74X_mcRun2_asymptotic_v2-v1", "RunIISpring15MiniAODv2", "Constant", 0.0189612, 240685),
        # private signal
        MCSample("T5HH_1200_200", "SusyRA2Analysis2015", "MiniAODv2", "Constant", 0.0856418, 48928),
        MCSample("T5HH_1200_950", "SusyRA2Analysis2015", "MiniAODv2", "Constant", 0.0856418, 48925),
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
	
    if applyWeight:
        print "Setup WeightProducer for '"+fileName+"'"

    return weightProducer
