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

def getWeightProducer(fileName,fastsim=False, pmssm=False):

    applyWeight = False
    
    ## --- Setup default WeightProducer ------------------------------------
    
    # Import weightProducer
    from TreeMaker.WeightProducer.weightProducer_cfi import weightProducer
    
    # Set default values to produce an event weight of 1
    weightProducer.weight = cms.double(1.0)
    weightProducer.Method = cms.string("Constant")
    weightProducer.FileNamePUDataDistribution = cms.string("NONE")

    # assign cross sections for fastsim
    # assume privately-produced samples do not have mixed mass points
    if fastsim and "SusyRA2Analysis2015" not in fileName:
        weightProducer.weight = cms.double(-1.)
        weightProducer.Method = cms.string("FastSim")
        weightProducer.NumberEvts = cms.double(1.0)
        if pmssm: weightProducer.modelIdentifier = cms.InputTag("Pmssm:PmssmId")
        else: weightProducer.modelIdentifier = cms.InputTag("SusyScan:SusyMotherMass")
        if "SMS-T1" in fileName or "SMS-T5" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_T1.txt")
        elif "SMS-T2tt" in fileName or "SMS-T2bb" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_T2.txt")
        elif "SMS-T2qq" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_T2qq.txt")
        elif "SMS-TChiHH" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_TChiHH.txt")
        elif "pMSSM_MCMC1" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/pmssm-xsecs-scan1.txt")
        print "Setup WeightProducer for '"+fileName+"'"
        return weightProducer
    
    # list of samples
    samples = [
        # 13 TeV miniAODv2 samples - Summer16
        # backgrounds
        # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
        # missing: TTJets inclusive
        # ttbar single lep & dilep xsecs scaled by PDG BR, assume t=tbar (hadronic: 377.96)
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 182.72, 61973977), # subtotal = 11957043
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 182.72, 61973977), # subtotal = 50016934
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 182.72, 60210394), # subtotal = 11944041
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 182.72, 60210394), # subtotal = 48266353
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 88.34, 30444678), # subtotal = 6094476
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 88.34, 30444678), # subtotal = 24350202
        MCSample("TTJets_SingleLeptFromT_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5.979, 17363624),
        # missing: TTJets_SingleLeptFromTbar_genMET-150
        MCSample("TTJets_DiLept_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.666, 9890329),
        # HT jets: GenXSecAnalyzer scaled by ttbar inclusive k-factor (NNLO vs MCM), 831.76/502.2 = 1.6562
        MCSample("TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 2.7343862, 14277035),
        MCSample("TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1.12075054, 10403610),
        MCSample("TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.1979159, 2932983),
        MCSample("TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.002368366, 1519815),
        # WJets: k-factor of 1.21 applied, extensions included
        MCSample("WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1627.45, 29503700),
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 435.24, 19766301), # subtotal = 4950373
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 435.24, 19766301), # subtotal = 14815928
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 59.18, 7759701), # subtotal = 1963464
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 59.18, 7759701), # subtotal = 5796237
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 14.58, 18687480), # subtotal = 3779141
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 14.58, 18687480), # subtotal = 14908339
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 6.66, 7745467), # subtotal = 1544513
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6.66, 7745467), # subtotal = 6200954
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1.608, 6872441), # subtotal = 244532
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1.608, 6872441), # subtotal = 6627909
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.03891, 2637821), # subtotal = 253561
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.03891, 2637821), # subtotal = 2384260
        # QCD: extensions included
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1717000, 57580393), # subtotal = 18722416
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1717000, 57580393), # subtotal = 38857977
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 351300, 54537903), # subtotal = 17035891
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 351300, 54537903), # subtotal = 37502012
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 31630, 62271343), # subtotal = 18929951
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 31630, 62271343), # subtotal = 43341392
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 6802, 45412780), # subtotal = 15629253
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6802, 45412780), # subtotal = 29783527
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1206, 15127293), # subtotal = 4767100
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1206, 15127293), # subtotal = 10360193
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 120.4, 11826702), # subtotal = 3970819
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 120.4, 11826702), # subtotal = 7855883
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 25.24, 6039005), # subtotal = 1991645
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 25.24, 6039005), # subtotal = 4047360
        # DY/Z: k-factor of 1.23 applied, available extensions included
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 181.302, 10607207), # subtotal = 2751187
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 181.302, 10607207), # subtotal = 7856020
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 50.4177, 9653731), # subtotal = 962195
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 50.4177, 9653731), # subtotal = 8691536
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 6.98394, 10008776), # subtotal = 1070454
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6.98394, 10008776), # subtotal = 8938322
        MCSample("DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 1.68141, 8292957),
        MCSample("DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.775392, 2668730),
        MCSample("DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.186222, 596079),
        MCSample("DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.00438495, 399492),
        MCSample("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 6025.2, 49144274),
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 344.8305, 24272858), # subtotal = 5246318
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 344.8305, 24272858), # subtotal = 19026540
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 95.5341, 24744916), # subtotal = 5132650
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 95.5341, 24744916), # subtotal = 19612266
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 13.1979, 9862869), # subtotal = 1020309
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 13.1979, 9862869), # subtotal = 8842560
        MCSample("ZJetsToNuNu_HT-600To800_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.14757, 5763506),
        MCSample("ZJetsToNuNu_HT-800To1200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1.450908, 2170137),
        MCSample("ZJetsToNuNu_HT-1200To2500_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.3546459, 513471), # subtotal = 369514
        MCSample("ZJetsToNuNu_HT-1200To2500_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.3546459, 513471), # subtotal = 143957
        MCSample("ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.00854235, 405030),
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 9226, 10182407), # subtotal = 5131873
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 9226, 10182407), # subtotal = 5050534
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2300, 20387336), # subtotal = 10036487
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 2300, 20387336), # subtotal = 10350849
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 277.4, 5060070), # subtotal = 2529729
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 277.4, 5060070), # subtotal = 2530341
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 93.38, 5080857), # subtotal = 2463946
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 93.38, 5080857), # subtotal = 2616911
        MCSample("GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5000, 14758163),
        MCSample("GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1079, 49572400),
        MCSample("GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 125.9, 11680386),
        MCSample("GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 43.36, 11639826),
        # single top: NoFullyHadronicDecays xsec scaled by BF for non-fully-hadronic (1-(1-3*0.108)^2
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.34, 622990), # straight total = 1000000
        MCSample("ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 136.02, 67240808),
        MCSample("ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 80.95, 38811017),
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 13576871), # subtotal = 5425134
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 13576871), # subtotal = 5425134
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 13576871), # subtotal = 2726603
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 11345619), # subtotal = 5372991
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 19.4674, 11345619), # subtotal = 3256650
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2", "RunIISummer16MiniAODv2", "Constant", 19.4674, 11345619), # subtotal = 2715978
        # rare backgrounds
        MCSample("WWTo2L2Nu_13TeV-powheg", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 12.178, 1999000),
        MCSample("WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 12.7, 5077680),
        MCSample("WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.834, 502190),
        MCSample("WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 49.997, 3223676), # straight total = 5176114
        MCSample("WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 10.71, 14017474), # straight total = 24152376
        MCSample("WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.058, 942046), # straight total = 1703772
        MCSample("ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 32.3, 1268806), # straight total = 2009042
        MCSample("ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.22, 9688612), # straight total = 15345572
        MCSample("ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 4.04, 18470622), # straight total = 30082038
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 0.2529, 927976), # straight total = 1992438
        MCSample("TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.5297, 351164), # straight total = 749400
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3", "RunIISummer16MiniAODv2", "Constant", 0.2043, 2716249), # subtotal = 1112722, straight subtotal = 2160168
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 0.2043, 2716249), # subtotal = 1603527, straight subtotal = 3120397
        MCSample("TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.4026, 430310), # straight total = 833298
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3.697, 4777013), # subtotal = 1577833, straight subtotal = 4870911
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 3.697, 4777013), # subtotal = 3199180, straight subtotal = 9885348
        MCSample("TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.009103, 104640), # straight total = 250000
        MCSample("WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.1651, 221468), # straight total = 250000
        MCSample("WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.05565, 216366), # straight total = 246800
        MCSample("ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.01398, 213197), # straight total = 249237
        # signal
        MCSample("SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.325388, 142671),
        MCSample("SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0141903, 142671),
        MCSample("SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0856418, 146849),
        MCSample("SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0141903, 105415),
        MCSample("SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.000981077, 51352),
        MCSample("SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.325388, 92094),
        MCSample("SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0252977, 51260),
        MCSample("SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1.31169, 156847),
        MCSample("SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.51848, 397678),
        MCSample("SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.0189612, 235029),
        MCSample("SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 36.3818, 949417),
        MCSample("SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 21.5949, 905836),
        MCSample("SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 21.5949, 899982),
        MCSample("SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 249.409, 400314),
        MCSample("SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 249.409, 291078),
        MCSample("SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 0.107045, 100070),

    
        # 13 TeV miniAODv1 samples - Spring16
        #backgrounds
        # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
        MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 831.76, 10259872),
        # ttbar single lep & dilep xsecs scaled by PDG BR, assume t=tbar (hadronic: 377.96)
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 182.72, 51873969), # subtotal = 11766102
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 182.72, 51873969), # subtotal = 40107867
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 182.72, 59654914), # subtotal = 11885875
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 182.72, 59654914), # subtotal = 47769039
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 88.34, 30587326), # subtotal = 6058236
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 88.34, 30587326), # subtotal = 24529090
        # HT jets: GenXSecAnalyzer scaled by ttbar inclusive k-factor (NNLO vs MCM), 831.76/502.2 = 1.6562
        MCSample("TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 2.7343862, 14305795),
        MCSample("TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 1.12075054, 10553666),
        MCSample("TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 0.1979159, 2932983),
        MCSample("TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.002368366, 523618),
        # WJets: k-factor of 1.21 applied, available extensions included
        MCSample("WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v2", "RunIISpring16MiniAODv1", "Constant", 1627.45, 29551425),
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2", "RunIISpring16MiniAODv1", "Constant", 435.24, 19966672), # subtotal = 4963240
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 435.24, 19966672), # subtotal = 15003432
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2", "RunIISpring16MiniAODv1", "Constant", 59.18, 7316767), # subtotal = 1963464
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 59.18, 7316767), # subtotal = 5353303
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2", "RunIISpring16MiniAODv1", "Constant", 14.58, 3723054),
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 6.66, 7480017), # subtotal = 1530092
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 6.66, 7480017), # subtotal = 5949925
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2", "RunIISpring16MiniAODv1", "Constant", 1.608, 246737),
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.03891, 252809),
        # QCD: extensions included
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 1717000, 55466657), # subtotal = 16650209
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 1717000, 55466657), # subtotal = 38816448
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 351300, 54703860), # subtotal = 16828258
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 351300, 54703860), # subtotal = 37875602
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 31630, 61558969), # subtotal = 17524810
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 31630, 61558969), # subtotal = 44034159
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 6802, 45453945), # subtotal = 15621634
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 6802, 45453945), # subtotal = 29832311
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 1206, 15217446), # subtotal = 4889688
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 1206, 15217446), # subtotal = 10327758
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 120.4, 11705926), # subtotal = 3928444
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 120.4, 11705926), # subtotal = 7777482
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 25.24, 6040004), # subtotal = 1992472
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v2", "RunIISpring16MiniAODv1", "Constant", 25.24, 6040004), # subtotal = 4047532
        # DY/Z: k-factor of 1.23 applied, available extensions included
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 181.302, 10628712), # subtotal = 2213426
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 181.302, 10628712), # subtotal = 8415286
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 50.4177, 9701936), # subtotal = 944458
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 50.4177, 9701936), # subtotal = 8757478
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1", "RunIISpring16MiniAODv2", "Constant", 6.98394, 8317271),
        MCSample("DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 2.70354, 5150414), # subtotal = 1034084
        MCSample("DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1", "RunIISpring16MiniAODv2", "Constant", 2.70354, 5150414), # subtotal = 4116330
        MCSample("DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 1.68141, 8232153),
        MCSample("DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 0.775392, 2650775),
        MCSample("DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 0.186222, 616612),
        MCSample("DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 0.00438495, 376260),
        MCSample("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 6025.2, 49868990),
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v2", "RunIISpring16MiniAODv1", "Constant", 344.8305, 18665303),
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v1", "RunIISpring16MiniAODv1", "Constant", 95.5341, 19914665),
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 13.1979, 1020309),
        MCSample("ZJetsToNuNu_HT-600To800_13TeV-madgraph", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 3.14757, 5650700),
        MCSample("ZJetsToNuNu_HT-800To1200_13TeV-madgraph", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 1.450908, 2156175),
        MCSample("ZJetsToNuNu_HT-1200To2500_13TeV-madgraph", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.3546459, 365216),
        MCSample("ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.00854235, 405752),
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2", "RunIISpring16MiniAODv1", "Constant", 9226, 5142782),
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 2300, 10296521),
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 277.4, 2528414),
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 93.38, 2459255),
        MCSample("GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 5000, 15405933),
        MCSample("GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 1079, 58878539),
        MCSample("GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 125.9, 18698921),
        MCSample("GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 43.36, 21493273),
        # rare backgrounds
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 3.34, 622990), # straight total = 1000000
        MCSample("ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 26.23, 1666000),
        MCSample("ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1", "RunIISpring16MiniAODv2", "Constant", 44.07, 3279200),
        MCSample("ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 35.6, 967600),
        MCSample("ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 35.6, 998400),
        MCSample("WWTo2L2Nu_13TeV-powheg", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 12.178, 1986200),
        MCSample("WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 49.997, 2807912), # straight total = 4508868
        MCSample("WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 10.71, 11214884), # straight total = 19309898
        MCSample("WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 3.058, 915022), # straight total = 1654964
        MCSample("ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 3.22, 9780613), # straight total = 15492017
        MCSample("ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 4.04, 18883640), # straight total = 30755844
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v3", "RunIISpring16MiniAODv1", "Constant", 0.2529, 185232), # straight total = 398600
        MCSample("TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.5297, 351164), # straight total = 749400
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.2043, 130275), # straight total = 252673
        MCSample("TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.4026, 430310), # straight total = 833298
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 3.697, 1578877), # straight total = 4874091
        MCSample("TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext1-v2", "RunIISpring16MiniAODv1", "Constant", 0.009103, 414865), # straight total = 993691
        MCSample("WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.1651, 220782), # straight total = 249200
        MCSample("WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.05565, 218986), # straight total = 249800
        MCSample("ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.01398, 213850), # straight total = 250000
        # missing: ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8
        # missing: ZH_HToBB_ZToNuNu_M125_13TeV_amcatnloFXFX_madspin_pythia8
        # missing: WH_HToBB_WToLNu_M125_13TeV_amcatnloFXFX_madspin_pythia8
        # signal
        MCSample("SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.325388, 142671),
        MCSample("SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.0141903, 52465),
        MCSample("SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.0856418, 146849),
        MCSample("SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.0141903, 105415),
        MCSample("SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2", "RunIISpring16MiniAODv2", "Constant", 0.325388, 92094),
        MCSample("SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2", "RunIISpring16MiniAODv2", "Constant", 0.0252977, 50869),
        MCSample("SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 1.31169, 156847),
        MCSample("SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.51848, 388225),
        MCSample("SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1", "RunIISpring16MiniAODv1", "Constant", 0.0189612, 227907),
    ]
    
    # loop over all samples until we find a match
    for sample in samples:
        if sample.name in fileName and sample.production in fileName:
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
