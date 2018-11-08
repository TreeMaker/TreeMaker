# $Id: getWeightProducer_cff.py,v 1.7 2012/11/05 14:58:14 mschrode Exp $
#
# Returns a WeightProducer module that knows at runtime
# which data sample is produced and thus, what weights
# are required.

import FWCore.ParameterSet.Config as cms
from TreeMaker.WeightProducer.MCSample import MCSample

def getWeightProducer(fileName,fastsim=False, pmssm=False):

    applyWeight = False
    
    ## --- Setup default WeightProducer ------------------------------------
    
    # Import weightProducer
    from TreeMaker.WeightProducer.weightProducer_cfi import weightProducer
    
    # Set default values to produce an event weight of 1
    weightProducer.weight = cms.double(1.0)
    weightProducer.Method = cms.string("Constant")
    weightProducer.SampleName = cms.string("")
    weightProducer.FileNamePUDataDistribution = cms.string("")
    weightProducer.FileNamePUMCDistribution = cms.string("")
    weightProducer.RemakePU = cms.bool(False)

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
        MCSample("TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10139950),
        # ttbar single lep & dilep
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 61973977), # subtotal = 11957043
        MCSample("TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 61973977), # subtotal = 50016934
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 60210394), # subtotal = 11944041
        MCSample("TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 60210394), # subtotal = 48266353
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 30444678), # subtotal = 6094476
        MCSample("TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 30444678), # subtotal = 24350202
        MCSample("TTJets_SingleLeptFromT_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 17363624),
        MCSample("TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 17264493),
        MCSample("TTJets_DiLept_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 9890329),
        # HT binned
        MCSample("TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 14277035),
        MCSample("TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 10403610),
        MCSample("TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 2932983),
        MCSample("TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1519815),
        # NLO powheg 
        MCSample("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 155235652), # subtotal = 77229341
        MCSample("TT_TuneCUETP8M2T4_13TeV-powheg-pythia8", "PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 155235652), # subtotal = 78006311
        # WJets: extensions included
        MCSample("WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 29503700),
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 19766301), # subtotal = 4950373
        MCSample("WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 19766301), # subtotal = 14815928
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 7759701), # subtotal = 1963464
        MCSample("WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 7759701), # subtotal = 5796237
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 18687480), # subtotal = 3779141
        MCSample("WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 18687480), # subtotal = 14908339
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 7745467), # subtotal = 1544513
        MCSample("WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 7745467), # subtotal = 6200954
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 6872441), # subtotal = 244532
        MCSample("WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6872441), # subtotal = 6627909
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2637821), # subtotal = 253561
        MCSample("WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 2637821), # subtotal = 2384260
        MCSample("WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 86731806), # subtotal = 29705748
        MCSample("WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 86731806), # subtotal = 57026058
        # QCD: extensions included
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 57580393), # subtotal = 18722416
        MCSample("QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 57580393), # subtotal = 38857977
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 54537903), # subtotal = 17035891
        MCSample("QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 54537903), # subtotal = 37502012
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 62271343), # subtotal = 18929951
        MCSample("QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 62271343), # subtotal = 43341392
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 45412780), # subtotal = 15629253
        MCSample("QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 45412780), # subtotal = 29783527
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 15127293), # subtotal = 4767100
        MCSample("QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 15127293), # subtotal = 10360193
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 11826702), # subtotal = 3970819
        MCSample("QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 11826702), # subtotal = 7855883
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 6039005), # subtotal = 1991645
        MCSample("QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6039005), # subtotal = 4047360
        # QCD pT-hat binned: extensions included
        MCSample("QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 9954370),
        MCSample("QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 14595570), # subtotal = 7608830
        MCSample("QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 14595570), # subtotal = 6986740
        MCSample("QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 12457308), # subtotal = 5748736
        MCSample("QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 12457308), # subtotal = 6708572
        MCSample("QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 14796774), # subtotal = 7838066
        MCSample("QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 14796774), # subtotal = 6958708
        MCSample("QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 22403620), # subtotal = 18253032
        MCSample("QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 22403620), # subtotal = 4150588
        MCSample("QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3959986),
        MCSample("QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 13519308), # subtotal = 9622896
        MCSample("QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 13519308), # subtotal = 3896412
        MCSample("QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 19697092), # subtotal = 15704980
        MCSample("QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 19697092), # subtotal = 3992112
        MCSample("QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 9981655), # subtotal = 6982586
        MCSample("QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 9981655), # subtotal = 2999069
        MCSample("QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 2873427), # subtotal = 2477018
        MCSample("QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2873427), # subtotal = 396409
        MCSample("QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1949724), # subtotal = 1552064
        MCSample("QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1949724), # subtotal = 397660
        MCSample("QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 996130), # subtotal = 596904
        MCSample("QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 996130), # subtotal = 399226
        MCSample("QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 391735),
        # DY/Z: available extensions included
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10607207), # subtotal = 2751187
        MCSample("DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 10607207), # subtotal = 7856020
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 9653731), # subtotal = 962195
        MCSample("DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 9653731), # subtotal = 8691536
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10008776), # subtotal = 1070454
        MCSample("DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 10008776), # subtotal = 8938322
        MCSample("DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 8292957),
        MCSample("DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2668730),
        MCSample("DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 596079),
        MCSample("DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 399492),
        MCSample("DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 49144274),
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 24272858), # subtotal = 5246318
        MCSample("ZJetsToNuNu_HT-100To200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 24272858), # subtotal = 19026540
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 24744916), # subtotal = 5132650
        MCSample("ZJetsToNuNu_HT-200To400_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 24744916), # subtotal = 19612266
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 9862869), # subtotal = 1020309
        MCSample("ZJetsToNuNu_HT-400To600_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 9862869), # subtotal = 8842560
        MCSample("ZJetsToNuNu_HT-600To800_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5763506),
        MCSample("ZJetsToNuNu_HT-800To1200_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2170137),
        MCSample("ZJetsToNuNu_HT-1200To2500_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 513471), # subtotal = 369514
        MCSample("ZJetsToNuNu_HT-1200To2500_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 513471), # subtotal = 143957
        MCSample("ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 405030),
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10182407), # subtotal = 5131873
        MCSample("GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 10182407), # subtotal = 5050534
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 20387336), # subtotal = 10036487
        MCSample("GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 20387336), # subtotal = 10350849
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5060070), # subtotal = 2529729
        MCSample("GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2", "RunIISummer16MiniAODv2", "Constant", 5060070), # subtotal = 2530341
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5080857), # subtotal = 2463946
        MCSample("GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 5080857), # subtotal = 2616911
        MCSample("GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 14758163),
        MCSample("GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 49572400),
        MCSample("GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 11680386),
        MCSample("GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 11639826),
        MCSample("ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 10164959), # subtotal = 5077952
        MCSample("ZJetsToNuNu_Zpt-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 10164959), # subtotal = 5087007
        MCSample("ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3956564), # subtotal = 1986102
        MCSample("ZJetsToNuNu_Zpt-200toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 3956564), # subtotal = 1970462
        # single top:
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1000000, 622990), # straight total = 1000000
        MCSample("ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2989199, 1884837), # straight total = 2989199
        MCSample("ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 67240808),
        MCSample("ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 38811017),
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 11408144), # subtotal = 5425134
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 11408144), # subtotal = 3256407
        MCSample("ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 11408144), # subtotal = 2726603
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 11345619), # subtotal = 5372991
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 11345619), # subtotal = 3256650
        MCSample("ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1", "80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2", "RunIISummer16MiniAODv2", "Constant", 11345619), # subtotal = 2715978
        MCSample("ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6933094),
        MCSample("ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 6952830),
        MCSample("tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 970479, 255903), # straight total = 970479
        # rare backgrounds
        MCSample("WW_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 7981136), # subtotal = 994012
        MCSample("WW_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 7981136), # subtotal = 6987124
        MCSample("WZ_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 3995828), # subtotal = 1000000
        MCSample("WZ_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 3995828), # subtotal = 2995828
        MCSample("ZZ_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1988098), # subtotal = 990064
        MCSample("ZZ_TuneCUETP8M1_13TeV-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 1988098), # subtotal = 998034
        MCSample("WWTo2L2Nu_13TeV-powheg", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1999000),
        MCSample("WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5077680),
        MCSample("WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 502190),
        MCSample("WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5176114, 3223676), # straight total = 5176114
        MCSample("WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 24152376, 14017474), # straight total = 24152376
        MCSample("WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1703772, 942046), # straight total = 1703772
        MCSample("ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2009042, 1268806), # straight total = 2009042
        MCSample("ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 15345572, 9688612), # straight total = 15345572
        MCSample("ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 30082038, 18470622), # straight total = 30082038
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 13908701, 6488085), # subtotal = 927976, straight subtotal = 1992438
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 13908701, 6488085), # subtotal = 2790463, straight subtotal = 5982035
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1", "RunIISummer16MiniAODv2", "Constant", 13908701, 6488085), # subtotal = 2769646, straight subtotal = 5934228
        MCSample("TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 749400, 351164), # straight total = 749400
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3", "RunIISummer16MiniAODv2", "Constant", 5280565, 2716249), # subtotal = 1112722, straight subtotal = 2160168
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 5280565, 2716249), # subtotal = 1603527, straight subtotal = 3120397
        MCSample("TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 833298, 430310), # straight total = 833298
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 14756259, 4777013), # subtotal = 1577833, straight subtotal = 4870911
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 14756259, 4777013), # subtotal = 3199180, straight subtotal = 9885348
        MCSample("ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 10045633, 2981359), # straight total = 10045633
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1", "RunIISummer16MiniAODv2", "Constant", 9794226, 2910760), # straight total = 9794226
        MCSample("TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2456040, 1023172), # straight total = 2456040
        MCSample("TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 100000),
        MCSample("TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 97232),
        MCSample("TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 100000),
        MCSample("TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 98692),
        MCSample("TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 99142),
        MCSample("TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 97855),
        MCSample("TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 98713),
        MCSample("WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 250000, 221468), # straight total = 250000
        MCSample("WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 246800, 216366), # straight total = 246800
        MCSample("ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 249237, 213197), # straight total = 249237
        # signal
        MCSample("SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 142671),
        MCSample("SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 52465),
        MCSample("SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 146849),
        MCSample("SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 105415),
        MCSample("SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 51352),
        MCSample("SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 92094),
        MCSample("SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 51260),
        MCSample("SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 156847),
        MCSample("SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 397678),
        MCSample("SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 235029),
        MCSample("SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 949417),
        MCSample("SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 905836),
        MCSample("SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 899982),
        MCSample("SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 400314),
        MCSample("SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 291078),
        MCSample("SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 100070),
        MCSample("SMS-T5qqqqWW_mGluino-1900_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 51188),
        MCSample("SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 4003007),
        MCSample("SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 396239), 
        MCSample("SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 413868),
        MCSample("SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 400482),
        MCSample("SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 408233),
        MCSample("SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 400887),
        MCSample("SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 394281),
        MCSample("SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 397668),
        MCSample("SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 414063),
        MCSample("SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 389625),
        MCSample("SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 404812),
        MCSample("SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 417293),
        MCSample("SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 391445),
        MCSample("SMS-T5qqqqZH-mGluino2200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 396083),
        # semivisible jet signals
        MCSample("step4_MINIAOD_mZprime-1000_mDark-20_rinv-0.3_alpha-0.2_n-1000", "", "", "Constant", 101734),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-0.2_n-1000", "", "", "Constant", 50686),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-0.1_n-1000", "", "", "Constant", 50485),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.5_alpha-0.2_n-1000", "", "", "Constant", 50977),
        MCSample("step4_MINIAOD_mZprime-2000_mDark-20_rinv-0.3_alpha-0.2_n-1000", "", "", "Constant", 51109),
        MCSample("step4_MINIAOD_mZprime-4000_mDark-20_rinv-0.3_alpha-0.2_n-1000", "", "", "Constant", 50998),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-1_rinv-0.3_alpha-0.2_n-1000", "", "", "Constant", 50700),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-50_rinv-0.3_alpha-0.2_n-1000", "", "", "Constant", 51089),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-100_rinv-0.3_alpha-0.2_n-1000", "", "", "Constant", 51000),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.1_alpha-0.2_n-1000", "", "", "Constant", 52779),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.7_alpha-0.2_n-1000", "", "", "Constant", 50733),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-0.5_n-1000", "", "", "Constant", 51081),
        MCSample("step4_MINIAOD_mZprime-3000_mDark-20_rinv-0.3_alpha-1_n-1000", "", "", "Constant", 50904),
        # stealth/rpv stop signals
        MCSample("stealth_stop_350_singlino_SYY", "", "", "Constant", 71695),
        MCSample("stealth_stop_450_singlino_SYY", "", "", "Constant", 66250),
        MCSample("stealth_stop_550_singlino_SYY", "", "", "Constant", 63434),
        MCSample("stealth_stop_650_singlino_SYY", "", "", "Constant", 62097),
        MCSample("stealth_stop_750_singlino_SYY", "", "", "Constant", 60023),
        MCSample("stealth_stop_850_singlino_SYY", "", "", "Constant", 59107),
        MCSample("stealth_stop_350_singlino_SHuHd", "", "", "Constant", 72270),
        MCSample("stealth_stop_450_singlino_SHuHd", "", "", "Constant", 66340),
        MCSample("stealth_stop_550_singlino_SHuHd", "", "", "Constant", 63399),
        MCSample("stealth_stop_650_singlino_SHuHd", "", "", "Constant", 61442),
        MCSample("stealth_stop_750_singlino_SHuHd", "", "", "Constant", 59992),
        MCSample("stealth_stop_850_singlino_SHuHd", "", "", "Constant", 59737),
        MCSample("rpv_stop_350_t3j_uds", "", "", "Constant", 69543),
        MCSample("rpv_stop_450_t3j_uds", "", "", "Constant", 64566),
        MCSample("rpv_stop_550_t3j_uds", "", "", "Constant", 61287),
        MCSample("rpv_stop_650_t3j_uds", "", "", "Constant", 59334),
        MCSample("rpv_stop_750_t3j_uds", "", "", "Constant", 58016),
        MCSample("rpv_stop_850_t3j_uds", "", "", "Constant", 57069),


        # 13 TeV miniAODv2 samples - Fall17
        # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
        # NLO powheg 
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 58420151, False), # subtotal = 28504600, straight subtotal = 28504600
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 58420151, False), # subtotal = 29915551, straight subtotal = 29915551
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 29501065, False),
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 29602576, False),
        # ttbar single lep & dilep xsecs scaled by PDG BR, assume t=tbar (hadronic: 377.96)
        MCSample('TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 61761347, True, 61692445),
        MCSample('TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 56705550, False, 56643562),
        MCSample('TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 28380110, False, 28349068),
        MCSample('TTJets_SingleLeptFromTbar_genMET-150_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 8233477, False, 8213871),
        # HT jets: GenXSecAnalyzer scaled by ttbar inclusive k-factor (NNLO vs MCM), 831.76/502.2 = 1.6562
        MCSample('TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v3', 'RunIIFall17MiniAODv2', 'Constant', 5155687, False, 4798753),
        # WJets: k-factor of 1.21 applied, extensions included
        MCSample('WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 35862893, False, 35804623),
        MCSample('WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 21250517, False, 21192211),
        MCSample('WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 14313274, False, 14250114),
        MCSample('WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 21709087, False, 21582309),
        MCSample('WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 20432728, False, 20272990),
        MCSample('WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 20258624, False, 19991892),
        MCSample('WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v3', 'RunIIFall17MiniAODv2', 'Constant', 21495421, False, 20629585),
        # QCD pT-hat binned: cross sections from AN2017_013_v17, extensions included
        MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 27957000, False),
        MCSample('QCD_Pt_120to170_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 29854280, False),
        MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 29829920, True),
        MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 111229780, True), # subtotal = 53798780, straight subtotal = 53798780
        MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v3', 'RunIIFall17MiniAODv2', 'Constant', 111229780, True), # subtotal = 57431000, straight subtotal = 57431000
        MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27881028, False),
        MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 66134964, True),
        MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 78116008, False), # subtotal = 39529008, straight subtotal = 39529008
        MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 78116008, False), # subtotal = 38587000, straight subtotal = 38587000
        MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2', 'RunIIFall17MiniAODv2', 'Constant', 35819814, True), # subtotal = 19631814, straight subtotal = 16188000
        MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 35819814, True), # subtotal = 16188000, straight subtotal = 19631814
        MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5685270, True),
        MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 2923941, True),
        MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 1910526, True),
        MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 757837, True),
        # QCD: extensions included
        MCSample('QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 58689666, True, 58623306),
        MCSample('QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 60316577, True, 60205669),
        MCSample('QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 56207744, False, 56041018),
        MCSample('QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 47724800, True, 47518924),
        MCSample('QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 16595628, True, 16485296),
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
        MCSample('GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 537295, False, 535335),
        MCSample('GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 26207004, False, 26163710),
        MCSample('GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 12028839, True, 12028589),
        MCSample('GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 8392881, False, 8361249),
        # single top: NoFullyHadronicDecays xsec scaled by BF for non-fully-hadronic (1-(1-3*0.108)^2
        MCSample('ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9568575, True, 5970607),
        MCSample('ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5865875, True),
        MCSample('ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 3939990, True),
        MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 11502515, True, 8399349), # subtotal = 5334538, straight subtotal = 5375230
        MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 11502515, True, 8399349), # subtotal = 3064811, straight subtotal = 6127285
        MCSample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4974435, True, 4936387),
        MCSample('ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 7780870, True, 7721566),
        MCSample('ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 7581624, True, 7523294),
        # rare backgrounds
        MCSample('WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 4121843, False, 4110545),
        MCSample('WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5054286, True, 3169582),
        MCSample('WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 19086373, False, 11347099),
        MCSample('WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4994395, False, 2717911),
        MCSample('ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27840918, False, 17768294),
        MCSample('TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 7563490, True, 3570720),
        MCSample('TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 750000, True, 356286),
        MCSample('TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4925829, True, 2678775),
        MCSample('TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 811306, True, 441560),
        MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 14026117, True, 5441639), # subtotal = 1795589, straight subtotal = 4623345
        MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1', 'RunIIFall17MiniAODv2', 'Constant', 14026117, True, 5441639), # subtotal = 3646050, straight subtotal = 9402772
        MCSample('ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9659185, True, 3324103),
        MCSample('ttHJetTobb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 9911561, True, 3409351),
        MCSample('TTGamma_SingleLeptFromT_TuneCP5_PSweights_13TeV_madgraph_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4911716, False, 4910406),
        MCSample('TTGamma_SingleLeptFromTbar_TuneCP5_PSweights_13TeV_madgraph_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4809392, False, 4807960),
        MCSample('TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4642344, False, 4641882),
        MCSample('TTTT_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_pilot_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 993804, True, 371504),
        MCSample('TTHH_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 199374),
        MCSample('TTTW_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 199704),
        MCSample('TTWH_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 198982),
        MCSample('TTWZ_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 198758),
        MCSample('TTZH_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 199286),
        MCSample('TTZZ_TuneCP5_13TeV-madgraph-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 200000, True, 199372),
        MCSample('WZZ_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 250000, True, 219660),
        MCSample('ZZZ_TuneCP5_13TeV-amcatnlo-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 250000, True, 213514),
        # signal
        MCSample('SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 91673, False),
        MCSample('SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 99440, False, 98520),
        MCSample('SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 222410, False),
        MCSample('SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 248828, False, 243114),
        MCSample('SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 250392, False, 231034),
        MCSample('SMS_TChiWH_WToLNu_HToBB_mChargino850_mLSP1_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 101040, False, 98806),
        MCSample('SMS-TChiWZ_ZToLL_mZMin-0p1_mChargino250_mLSP230_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 106831, False, 106515),
        # stealth/rpv stop signals
        MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 507649, False),
        MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 523220, False, 521846),
        MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 210725, False),
        MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 220618, False, 219422),
        MCSample('StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 215579, False, 214375),
        MCSample('StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 211657, False, 210577),
        MCSample('StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 532773, False, 531723),
        MCSample('StealthSHH_2t4b_mStop-350_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 566558, False, 565120),
    ]
    
    # loop over all samples until we find a match
    for sample in samples:
        if sample.name in fileName and sample.production in fileName:
            weightProducer.Method     = cms.string(sample.Method)
            weightProducer.XS         = cms.double(sample.XS)
            weightProducer.NumberEvts = cms.double(sample.NumberEvtsDiff)
            weightProducer.RemakePU   = cms.bool(sample.WrongPU)
            print sample.name+", "+sample.production+" : '"+fileName+"'"
            applyWeight = True
            weightProducer.weight = cms.double(-1.)
            break
	
    if applyWeight:
        print "Setup WeightProducer for '"+fileName+"'"

    return weightProducer
