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
    samples = []
    from MCSamples_Summer16 import Summer16samples
    from MCSamples_Fall17 import Fall17samples
    from MCSamples_Summer16v3 import Summer16v3samples
    from MCSamples_Autumn18 import Autumn18samples
    from SVJsamples import SVJsamples
    samples += Summer16samples
    samples += Fall17samples
    samples += Summer16v3samples
    samples += Autumn18samples
    samples += SVJsamples
    
    # loop over all samples until we find a match
    for sample in samples:
        if sample.name in fileName and sample.production in fileName:
            weightProducer.Method     = cms.string(sample.Method)
            weightProducer.XS         = cms.double(sample.XS*sample.BR*sample.kFactor*sample.corr)
            weightProducer.NumberEvts = cms.double(sample.NumberEvtsDiff)
            weightProducer.RemakePU   = cms.bool(sample.WrongPU)
            print sample.name+", "+sample.production+" : '"+fileName+"'"
            applyWeight = True
            weightProducer.weight = cms.double(-1.)
            break
	
    if applyWeight:
        print "Setup WeightProducer for '"+fileName+"'"

    return weightProducer
