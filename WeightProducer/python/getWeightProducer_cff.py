# $Id: getWeightProducer_cff.py,v 1.7 2012/11/05 14:58:14 mschrode Exp $
#
# Returns a WeightProducer module that knows at runtime
# which data sample is produced and thus, what weights
# are required.

import FWCore.ParameterSet.Config as cms
from TreeMaker.WeightProducer.MCSample import MCSample

def getWeightProducer(fileName, scan=False):

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

    # assign cross sections for signal scans
    if scan:
        weightProducer.weight = cms.double(-1.)
        weightProducer.Method = cms.string("SignalScan")
        weightProducer.NumberEvts = cms.double(1.0)
        weightProducer.modelIdentifier = cms.InputTag("SignalScan:SignalParameters")
        if "SMS-T1" in fileName or "SMS-T5" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_T1_NNLO.txt")
        elif "SMS-T2tt" in fileName or "SMS-T2bb" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_T2_NNLO.txt")
        elif "SMS-T2qq" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_T2qq_NNLO.txt")
        elif "SMS-TChiHH" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_TChiHH.txt")
        elif "pMSSM_MCMC1" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/pmssm-xsecs-scan1.txt")
        elif "SVJ" in fileName: weightProducer.XsecFile = cms.string("TreeMaker/Production/test/data/dict_xsec_Zprime.txt")
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
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8', 'PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1', 'RunIISummer16MiniAODv2', 'Constant', 156469815, False), # subtotal = 59033604
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8', 'PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1', 'RunIISummer16MiniAODv2', 'Constant', 156469815, False), # subtotal = 97436211
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
        MCSample("ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1000000, False, 622990), # straight total = 1000000
        MCSample("ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2989199, False, 1884837), # straight total = 2989199
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
        MCSample("tZq_W_lept_Z_hadron_4f_ckm_NLO_13TeV_amcatnlo_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 970479, False, 255903), # straight total = 970479
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
        MCSample("WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 5176114, False, 3223676), # straight total = 5176114
        MCSample("WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 24152376, False, 14017474), # straight total = 24152376
        MCSample("WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 1703772, False, 942046), # straight total = 1703772
        MCSample("ZGTo2NuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2009042, False, 1268806), # straight total = 2009042
        MCSample("ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 15345572, False, 9688612), # straight total = 15345572
        MCSample("ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 30082038, False, 18470622), # straight total = 30082038
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 13908701, False, 6488085), # subtotal = 927976, straight subtotal = 1992438
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 13908701, False, 6488085), # subtotal = 2790463, straight subtotal = 5982035
        MCSample("TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1", "RunIISummer16MiniAODv2", "Constant", 13908701, False, 6488085), # subtotal = 2769646, straight subtotal = 5934228
        MCSample("TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 749400, False, 351164), # straight total = 749400
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v3", "RunIISummer16MiniAODv2", "Constant", 5280565, False, 2716249), # subtotal = 1112722, straight subtotal = 2160168
        MCSample("TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1", "RunIISummer16MiniAODv2", "Constant", 5280565, False, 2716249), # subtotal = 1603527, straight subtotal = 3120397
        MCSample("TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 833298, False, 430310), # straight total = 833298
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 14756259, False, 4777013), # subtotal = 1577833, straight subtotal = 4870911
        MCSample("TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 14756259, False, 4777013), # subtotal = 3199180, straight subtotal = 9885348
        MCSample("ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1", "RunIISummer16MiniAODv2", "Constant", 10045633, False, 2981359), # straight total = 10045633
        MCSample("ttHJetTobb_M125_13TeV_amcatnloFXFX_madspin_pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext3-v1", "RunIISummer16MiniAODv2", "Constant", 9794226, False, 2910760), # straight total = 9794226
        MCSample("TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 2456040, False, 1023172), # straight total = 2456040
        MCSample("TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 100000),
        MCSample("TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 97232),
        MCSample("TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 100000),
        MCSample("TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3", "RunIISummer16MiniAODv2", "Constant", 98692),
        MCSample("TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 99142),
        MCSample("TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 97855),
        MCSample("TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2", "RunIISummer16MiniAODv2", "Constant", 98713),
        MCSample('TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8', 'PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2', 'RunIISummer16MiniAODv2', 'Constant', 96288, False),
        MCSample("WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 250000, False, 221468), # straight total = 250000
        MCSample("WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 246800, False, 216366), # straight total = 246800
        MCSample("ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8", "PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1", "RunIISummer16MiniAODv2", "Constant", 249237, False, 213197), # straight total = 249237
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
        # rare backgrounds
        MCSample('WGJets_MonoPhoton_PtG-40to130_TuneCP5_13TeV-madgraph', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 4121843, False, 4110545),
        MCSample('WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 5054286, True, 3169582),
        MCSample('WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 19086373, False, 11347099),
        MCSample('WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 4994395, False, 2717911),
        MCSample('ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27840918, False, 17768294),
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
        # stealth/rpv stop signals
        MCSample('RPV_2t6j_mStop-300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 511693, False),
        MCSample('RPV_2t6j_mStop-300_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 533878, False, 532748),
        MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 507649, False),
        MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 523220, False, 521846),
        MCSample('RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 460837, False),
        MCSample('RPV_2t6j_mStop-400_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 553126, False, 551420),
        MCSample('RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 381796, False),
        MCSample('RPV_2t6j_mStop-450_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 388250, False, 386558),
        MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 210725, False),
        MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 220618, False, 219422),
        MCSample('RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 123462, False),
        MCSample('RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 126676, False, 125906),
        MCSample('RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 73189, False),
        MCSample('RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 79816, False, 79158),
        MCSample('RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 51755, False),
        MCSample('RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v2', 'RunIIFall17MiniAODv2', 'Constant', 56056, False, 55514),
        MCSample('RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 51218, False),
        MCSample('RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 51093, False, 50499),
        MCSample('RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 50807, False),
        MCSample('RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 52800, False, 51998),
        MCSample('RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 26030, False),
        MCSample('RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27606, False, 27104),
        MCSample('RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 26545, False),
        MCSample('RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27810, False, 27156),
        MCSample('RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8', 'PU2017_12Apr2018_94X_mc2017_realistic_v14-v1', 'RunIIFall17MiniAODv2', 'Constant', 27490, False),
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

        # 13 TeV miniAODv3 samples - Summer16
        # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
        MCSample('TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 10199051, False),
        MCSample('TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 61621218, False), # subtotal = 11957043
        MCSample('TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 61621218, False), # subtotal = 49664175
        MCSample('TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4302086, False),
        MCSample('TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 60343752, False), # subtotal = 11955887
        MCSample('TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 60343752, False), # subtotal = 48387865
        MCSample('TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4310038, False),
        MCSample('TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 30836035, False), # subtotal = 6068369
        MCSample('TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 30836035, False), # subtotal = 24767666
        MCSample('TTJets_SingleLeptFromT_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 17355657, False),
        MCSample('TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 17003930, False),
        MCSample('TTJets_DiLept_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9753471, False),
        MCSample('TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 14344298, False),
        MCSample('TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 10529747, False),
        MCSample('TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 2932983, False),
        MCSample('TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 1519815, False),
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 29602576, False),
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 59133437, False), # subtotal = 29632372
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 59133437, False), # subtotal = 29501065
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 58420151, False), # subtotal = 28504600
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 58420151, False), # subtotal = 29915551
        MCSample('TT_TuneCUETP8M2T4_13TeV-powheg-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 76915549, False),
        MCSample('TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 79140880, False),
        MCSample('WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 86916455, False), # subtotal = 29514020
        MCSample('WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2', 'RunIISummer16MiniAODv3', 'Constant', 86916455, False), # subtotal = 57402435
        MCSample('WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 10020533, False),
        MCSample('WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9945478, False),
        MCSample('WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 38984322, False), # subtotal = 4963240
        MCSample('WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 38984322, False), # subtotal = 14106492
        MCSample('WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2', 'RunIISummer16MiniAODv3', 'Constant', 38984322, False), # subtotal = 19914590
        MCSample('WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 7759701, False), # subtotal = 1963464
        MCSample('WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 7759701, False), # subtotal = 5796237
        MCSample('WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 18687480, False), # subtotal = 3779141
        MCSample('WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 18687480, False), # subtotal = 14908339
        MCSample('WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 7830536, False), # subtotal = 1544513
        MCSample('WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 7830536, False), # subtotal = 6286023
        MCSample('WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 6872441, False), # subtotal = 244532
        MCSample('WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 6872441, False), # subtotal = 6627909
        MCSample('WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 2637821, False), # subtotal = 253561
        MCSample('WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 2637821, False), # subtotal = 2384260
        MCSample('QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 6696872, False),
        MCSample('QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 12616158, False), # subtotal = 6867422
        MCSample('QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 12616158, False), # subtotal = 5748736
        MCSample('QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 14796774, False), # subtotal = 6958708
        MCSample('QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 14796774, False), # subtotal = 7838066
        MCSample('QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 22470404, False), # subtotal = 4150588
        MCSample('QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 22470404, False), # subtotal = 18319816
        MCSample('QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 3959986, False),
        MCSample('QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 13524747, False), # subtotal = 3896412
        MCSample('QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 13524747, False), # subtotal = 9628335
        MCSample('QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 19697092, False), # subtotal = 3992112
        MCSample('QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 19697092, False), # subtotal = 15704980
        MCSample('QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 9846615, False), # subtotal = 2999069
        MCSample('QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 9846615, False), # subtotal = 6847546
        MCSample('QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 2873427, False), # subtotal = 396409
        MCSample('QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 2873427, False), # subtotal = 2477018
        MCSample('QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 1982038, False), # subtotal = 397660
        MCSample('QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 1982038, False), # subtotal = 1584378
        MCSample('QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 996130, False), # subtotal = 399226
        MCSample('QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 996130, False), # subtotal = 596904
        MCSample('QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 391735, False),
        MCSample('QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 4141251, False),
        MCSample('QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 31878740, False),
        MCSample('QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 29954815, False),
        MCSample('QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 19662175, False),
        MCSample('QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 13895437, False),
        MCSample('QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 7897731, False),
        MCSample('QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 7947159, False),
        MCSample('QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 7937590, False),
        MCSample('QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 3972819, False),
        MCSample('QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 4010136, False),
        MCSample('QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 3962749, False),
        MCSample('QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 3990117, False),
        MCSample('QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'ConstantFlat', 19996995, False),
        MCSample('QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8', 'HEM_102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'ConstantFlat', 18688995, False),
        MCSample('QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 57580393, False), # subtotal = 18722416
        MCSample('QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 57580393, False), # subtotal = 38857977
        MCSample('QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 54552852, False), # subtotal = 17035891
        MCSample('QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 54552852, False), # subtotal = 37516961
        MCSample('QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 62622029, False), # subtotal = 18560541
        MCSample('QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 62622029, False), # subtotal = 44061488
        MCSample('QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 15629253, False),
        MCSample('QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 15210939, False), # subtotal = 4850746
        MCSample('QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 15210939, False), # subtotal = 10360193
        MCSample('QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 11839357, False), # subtotal = 3970819
        MCSample('QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 11839357, False), # subtotal = 7868538
        MCSample('QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 6019541, False), # subtotal = 1991645
        MCSample('QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 6019541, False), # subtotal = 4027896
        MCSample('DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 11017086, False), # subtotal = 2751187
        MCSample('DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 11017086, False), # subtotal = 8265899
        MCSample('DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9609137, False), # subtotal = 962195
        MCSample('DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 9609137, False), # subtotal = 8646942
        MCSample('DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9725661, False), # subtotal = 1070454
        MCSample('DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 9725661, False), # subtotal = 8655207
        MCSample('DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 8292957, False),
        MCSample('DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 2673066, False),
        MCSample('DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 596079, False),
        MCSample('DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 399492, False),
        MCSample('DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 49748967, False),
        MCSample('ZJetsToNuNu_HT-100To200_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 24272858, False), # subtotal = 5246318
        MCSample('ZJetsToNuNu_HT-100To200_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 24272858, False), # subtotal = 19026540
        MCSample('ZJetsToNuNu_HT-200To400_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 24761211, False), # subtotal = 5136083
        MCSample('ZJetsToNuNu_HT-200To400_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 24761211, False), # subtotal = 19625128
        MCSample('ZJetsToNuNu_HT-400To600_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 9862869, False), # subtotal = 1020309
        MCSample('ZJetsToNuNu_HT-400To600_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 9862869, False), # subtotal = 8842560
        MCSample('ZJetsToNuNu_HT-600To800_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 5766322, False),
        MCSample('ZJetsToNuNu_HT-800To1200_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 2170137, False),
        MCSample('ZJetsToNuNu_HT-1200To2500_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 513471, False), # subtotal = 369514
        MCSample('ZJetsToNuNu_HT-1200To2500_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 513471, False), # subtotal = 143957
        MCSample('ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 405030, False),
        MCSample('GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 10104155, False), # subtotal = 5131873
        MCSample('GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 10104155, False), # subtotal = 4972282
        MCSample('GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 20527506, False), # subtotal = 10122599
        MCSample('GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 20527506, False), # subtotal = 10404907
        MCSample('GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 5060070, False), # subtotal = 2529729
        MCSample('GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 5060070, False), # subtotal = 2530341
        MCSample('GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 5080857, False), # subtotal = 2463946
        MCSample('GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 5080857, False), # subtotal = 2616911
        MCSample('GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 14821862, False),
        MCSample('GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 50002467, False),
        MCSample('GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 11702604, False),
        MCSample('GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_qcut19_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 11687048, False),
        MCSample('ST_s-channel_4f_InclusiveDecays_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 2989199, False, 1884837),
        MCSample('ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 1000000, False, 622990),
        MCSample('ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 67105876, False),
        MCSample('ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 38811017, False),
        MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 3256407, False),
        MCSample('ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 3256650, False),
        MCSample('ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 6933094, False),
        MCSample('ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 998276, False),
        MCSample('ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 6952830, False),
        MCSample('ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 992024, False),
        MCSample('WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 5077680, False),
        MCSample('WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 502190, False),
        MCSample('WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 5246469, False, 3267135),
        MCSample('WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 24311445, False, 14109151),
        MCSample('WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 1703772, False, 942046),
        MCSample('ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 30493038, False, 18722534),
        MCSample('ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 15462693, False, 9762305),
        MCSample('TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1', 'RunIISummer16MiniAODv3', 'Constant', 5837781, False, 2723203),
        MCSample('TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 749400, False, 351164),
        MCSample('TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1', 'RunIISummer16MiniAODv3', 'Constant', 3120397, False, 1603527),
        MCSample('TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 833298, False, 430310),
        MCSample('TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 14748853, False, 4774447), # subtotal = 1577833, straight subtotal = 4870911
        MCSample('TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2', 'RunIISummer16MiniAODv3', 'Constant', 14748853, False, 4774447), # subtotal = 3196614, straight subtotal = 9877942
        MCSample('TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 4845923, False),
        MCSample('TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4846427, False),
        MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-fsrdown-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4944950, False),
        MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-fsrup-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4810617, False),
        MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-isrdown-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4964008, False),
        MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-isrup-pythia8-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4867940, False),
        MCSample('TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4873181, False),
        MCSample('TTGamma_Dilept_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 4773650, False),
        MCSample('TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 2456040, False, 1023172),
        MCSample('TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1', 'RunIISummer16MiniAODv3', 'Constant', 98300, False),
        MCSample('WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 240000, False, 210538),
        MCSample('WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 250000, False, 221468),
        MCSample('WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 246800, False, 216366),
        MCSample('ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 249237, False, 213197),
        MCSample('SMS-T1tttt_mGluino-1200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 146849, False),
        MCSample('SMS-T1tttt_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 105415, False),
        MCSample('SMS-T1tttt_mGluino-2000_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 51352, False),
        MCSample('SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 92094, False),
        MCSample('SMS-T1qqqq_mGluino-1400_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 51260, False),
        MCSample('SMS-T1qqqq_mGluino-1800_mLSP-200_ctau-1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 49841, False),
        MCSample('SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 142671, False),
        MCSample('SMS-T1bbbb_mGluino-1500_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 52465, False),
        MCSample('SMS-T2tt_mStop-150_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 827787, False),
        MCSample('SMS-T2tt_mStop-200_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 1001170, False),
        MCSample('SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 949417, False),
        MCSample('SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 905836, False),
        MCSample('SMS-T2tt_mStop-250_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 899982, False),
        MCSample('SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 400314, False),
        MCSample('SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 291078, False),
        MCSample('SMS-T2tt_mStop-350_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 189173, False),
        MCSample('SMS-T2tt_mStop-425_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 156847, False),
        MCSample('SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 397678, False),
        MCSample('SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 100070, False),
        MCSample('SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 235029, False),
        MCSample('SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 396239, False),
        MCSample('SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 413868, False),
        MCSample('SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 400482, False),
        MCSample('SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 408233, False),
        MCSample('SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 400887, False),
        MCSample('SMS-T5qqqqZH-mGluino1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 394281, False),
        MCSample('SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 397668, False),
        MCSample('SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 414063, False),
        MCSample('SMS-T5qqqqZH-mGluino1800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 389625, False),
        MCSample('SMS-T5qqqqZH-mGluino1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 404812, False),
        MCSample('SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 417293, False),
        MCSample('SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 391445, False),
        MCSample('SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 400307, False),
        MCSample('RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 417575, False),
        MCSample('RPV_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 370241, False),
        MCSample('RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 436873, False),
        MCSample('RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 319494, False),
        MCSample('RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 166908, False),
        MCSample('RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 100002, False),
        MCSample('RPV_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 62526, False),
        MCSample('RPV_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 44742, False),
        MCSample('RPV_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 43352, False),
        MCSample('RPV_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 43618, False),
        MCSample('RPV_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 21870, False),
        MCSample('RPV_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 21774, False),
        MCSample('RPV_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 21859, False),
        MCSample('StealthSYY_2t6j_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 450097, False),
        MCSample('StealthSYY_2t6j_mStop-350_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 386821, False),
        MCSample('StealthSYY_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 452809, False),
        MCSample('StealthSYY_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 324546, False),
        MCSample('StealthSYY_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 187464, False),
        MCSample('StealthSYY_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 36753, False),
        MCSample('StealthSYY_2t6j_mStop-600_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 67743, False),
        MCSample('StealthSYY_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 45578, False),
        MCSample('StealthSYY_2t6j_mStop-700_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 46223, False),
        MCSample('StealthSYY_2t6j_mStop-750_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 45409, False),
        MCSample('StealthSYY_2t6j_mStop-800_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 21232, False),
        MCSample('StealthSYY_2t6j_mStop-850_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 22607, False),
        MCSample('StealthSYY_2t6j_mStop-900_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 21995, False),
        MCSample('StealthSHH_2t4b_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 447416, False),
        MCSample('StealthSHH_2t4b_mStop-350_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 419903, False),
        MCSample('StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 449988, False),
        MCSample('StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 321284, False),
        MCSample('StealthSHH_2t4b_mStop-500_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 187680, False),
        MCSample('StealthSHH_2t4b_mStop-550_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 106106, False),
        MCSample('StealthSHH_2t4b_mStop-600_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 66786, False),
        MCSample('StealthSHH_2t4b_mStop-650_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 46652, False),
        MCSample('StealthSHH_2t4b_mStop-700_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 45627, False),
        MCSample('StealthSHH_2t4b_mStop-750_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 44131, False),
        MCSample('StealthSHH_2t4b_mStop-800_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 21785, False),
        MCSample('StealthSHH_2t4b_mStop-850_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v1', 'RunIISummer16MiniAODv3', 'Constant', 22727, False),
        MCSample('StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8', 'PUMoriond17_94X_mcRun2_asymptotic_v3-v2', 'RunIISummer16MiniAODv3', 'Constant', 8410, False),

        # 13 TeV miniAOD samples - Autumn18
        # NB: amcatnlo samples have negative weight events, so NumberEvts = # positive - # negative
        MCSample('TTJets_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10244307, False, 10234409),
        MCSample('TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 59929205, False, 59872080),
        MCSample('TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 57259880, False, 57205136),
        MCSample('TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 28701360, False, 28674428),
        MCSample('TTJets_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 14149394, False, 14065202),
        MCSample('TTJets_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10372802, False, 10282774),
        MCSample('TTJets_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 2779427, False, 2735863),
        MCSample('TTJets_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 1451104, False, 1376490),
        MCSample('QCD_Pt_80to120_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 29535000, False),
        MCSample('QCD_Pt_120to170_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 25255000, False),
        MCSample('QCD_Pt_170to300_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 29710000, False),
        MCSample('QCD_Pt_300to470_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 41744000, False),
        MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 42459973, False), # subtotal = 17712000, straight subtotal = 17712000
        MCSample('QCD_Pt_470to600_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 42459973, False), # subtotal = 24747973, straight subtotal = 24747973
        MCSample('QCD_Pt_600to800_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 64061000, False),
        MCSample('QCD_Pt_800to1000_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 37598000, False),
        MCSample('QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 18485000, False),
        MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 6928000, False), # subtotal = 2160000, straight subtotal = 2160000
        MCSample('QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 6928000, False), # subtotal = 4768000, straight subtotal = 4768000
        MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4017800, False), # subtotal = 1445800, straight subtotal = 1445800
        MCSample('QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 4017800, False), # subtotal = 2572000, straight subtotal = 2572000
        MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 2394000, False), # subtotal = 1440000, straight subtotal = 1440000
        MCSample('QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 2394000, False), # subtotal = 954000, straight subtotal = 954000
        MCSample('QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 800000, False),
        MCSample('QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 4576065, False),
        MCSample('QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v4', 'RunIIAutumn18MiniAOD', 'Constant', 30612338, False),
        MCSample('QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 29884616, False),
        MCSample('QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 20268872, False),
        MCSample('QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 612919, False),
        MCSample('QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 633668, False),
        MCSample('QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 35978539, False),
        MCSample('QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v3', 'RunIIAutumn18MiniAOD', 'Constant', 492418, False),
        MCSample('QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 16618977, False),
        MCSample('QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10719790, False),
        MCSample('QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 19996995, False),
        MCSample('QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8', 'HEM_102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 18688995, False),
        MCSample('QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 54289442, False, 54251666),
        MCSample('QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 54661579, False, 54600685),
        MCSample('QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 55152960, False, 55056202),
        MCSample('QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 48158738, False, 48038740),
        MCSample('QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 15466225, False, 15407797),
        MCSample('QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 10955087, False, 10887751),
        MCSample('QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 5475677, False, 5414545),
        MCSample('DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 11530510, False, 11518130),
        MCSample('DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 427051, False, 415713),
        MCSample('DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 11225887, False, 11206441),
        MCSample('DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 9643184, False, 9616642),
        MCSample('DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 8862104, False, 8828622),
        MCSample('DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 3138129, False, 3121975),
        MCSample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 100194597, False, 100114408),
        MCSample('DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v2', 'RunIIAutumn18MiniAOD', 'Constant', 507624, False, 503192),
        MCSample('WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 29521158, False, 29488310),
        MCSample('WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 25468933, False, 25423156),
        MCSample('WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 3273980, False, 3191612),
        MCSample('WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 5932701, False, 5915969),
        MCSample('WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 19771294, False, 19699782),
        MCSample('WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 28084244, False, 28060304),
        MCSample('WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 8402687, False, 8362227),
        MCSample('WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 7633949, False, 7571583),
        MCSample('ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 359639, False, 350333),
        MCSample('ZJetsToNuNu_HT-100To200_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 23702894, False, 23678782),
        MCSample('ZJetsToNuNu_HT-200To400_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 23276346, False, 23236674),
        MCSample('ZJetsToNuNu_HT-400To600_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 2707156, False, 2699566),
        MCSample('ZJetsToNuNu_HT-600To800_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 5748975, False, 5728007),
        MCSample('ZJetsToNuNu_HT-800To1200_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 2066798, False, 2056362),
        MCSample('ZJetsToNuNu_HT-1200To2500_13TeV-madgraph', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 343198, False, 340302),
        MCSample('GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '4cores5k_102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 9798176, False, 9796870),
        MCSample('GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 19062809, False, 19055655),
        MCSample('GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4655985, False, 4652345),
        MCSample('GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 4981121, False, 4971983),
        MCSample('GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 15424758, False, 15423022),
        MCSample('GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 49457520, False, 49438028),
        MCSample('GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 13717985, False, 13705653),
        MCSample('GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 12456593, False, 12431845),
        MCSample('ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v3', 'RunIIAutumn18MiniAOD', 'Constant', 19965000, False, 12458638),
        MCSample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1086487, False, 1081535),
        MCSample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 1085847, False, 1080939),
        MCSample('ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 7623000, False, 7588180),
        MCSample('ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15_ext1-v1', 'RunIIAutumn18MiniAOD', 'Constant', 9598000, False, 9553912),
        MCSample('WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4683136, False, 2941220),
        MCSample('WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 1690064, False, 920352),
        MCSample('ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 27900469, False, 17815224),
        MCSample('TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 4691915, False, 1842387),
        MCSample('TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 4911941, False, 2686095),
        MCSample('TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 835296, False, 458226),
        MCSample('TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 750000, False, 355226),
        MCSample('TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 13280000, False, 6274046),
        MCSample('TTWW_TuneCP5_13TeV-madgraph-pythia8', '102X_upgrade2018_realistic_v15_ext1-v2', 'RunIIAutumn18MiniAOD', 'Constant', 185000, False, 184094),
        MCSample('TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 64310000, False, 63791484),
        MCSample('TTToHadronic_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 133808000, False, 132725582),
        MCSample('TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8', '102X_upgrade2018_realistic_v15-v1', 'RunIIAutumn18MiniAOD', 'Constant', 101550000, False, 100728760),
    ]

    from SVJsamples import SVJsamples
    samples += SVJsamples
    
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
