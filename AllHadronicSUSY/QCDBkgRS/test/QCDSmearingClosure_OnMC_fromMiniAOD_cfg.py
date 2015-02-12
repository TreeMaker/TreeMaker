# Expects a file name as argument e.g.
# cmsRun mcresolutions_cfg.py data_set=/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM, global_tag=PHYS14_25_V1

## --- Read parameters --------------------------------------------------
from AllHadronicSUSY.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()

runOnMC = parameters.value("is_mc",True)
dataSetName = parameters.value("data_set","/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM")
testFileName = parameters.value("test_file_name","/store/mc/Phys14DR/QCD_Pt-15to3000_Tune4C_Flat_13TeV_pythia8/MINIAODSIM/PU20bx25_trkalmb_PHYS14_25_V1-v1/00000/1020E374-B26B-E411-8F91-E0CB4E29C513.root")
globalTag = parameters.value("global_tag","PHYS14_25_V1")+"::All"
lumi = parameters.value("lumi",4.0)
doPUReweighting = parameters.value("pu_reweighting",False)
InputJetTag = parameters.value("jet_tag","slimmedJets")
OutputFileName = parameters.value("out_name","QCDSmearingClosure_OnMC.root")

print "*** JOB SETUP ****************************************************"
print "  is_mc          : "+str(runOnMC)
print "  data_set       : "+dataSetName
print "  global_tag     : "+globalTag
print "  lumi           : "+str(lumi)
print "  pu_reweighting : "+str(doPUReweighting)
print "  jet_tag        : "+InputJetTag
print "  out_name       : "+OutputFileName
print "******************************************************************"

## --- The process needs to be defined AFTER reading sys.argv, ---------
## --- otherwise edmConfigHash fails -----------------------------------
import FWCore.ParameterSet.Config as cms
process = cms.Process("RA2QCDSmearingClosure")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = globalTag

## --- Log output ------------------------------------------------------
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr = cms.untracked.PSet(placeholder = cms.untracked.bool(True))
process.MessageLogger.cout = cms.untracked.PSet(INFO = cms.untracked.PSet(reportEvery = cms.untracked.int32(1000)))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

## --- Input Source ----------------------------------------------------
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring(testFileName))
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

## --- Setup WeightProducer --------------------------------------------
from AllHadronicSUSY.WeightProducer.getWeightProducer_cff import getWeightProducer
process.WeightProducer = getWeightProducer(dataSetName)
process.WeightProducer.Lumi = cms.double(lumi)
process.WeightProducer.PU = cms.int32(0) # PU: 3 for S10, 2 for S7
process.WeightProducer.FileNamePUDataDistribution = cms.string("NONE")

###############################################################################
process.TFileService = cms.Service("TFileService",fileName = cms.string("QCDSmearingClosure_OnMC.root") )
###############################################################################

###############################################################################
process.load("AllHadronicSUSY.QCDBkgRS.qcdbkgrs_cfi")
###############################################################################

###############################################################################
# Rebalancing and Smearing configuration
###############################################################################
process.QCDfromSmearing.SmearingFile = '/afs/desy.de/user/c/csander/xxl-af-cms/CMSSW_7_2_3_patch1/src/AllHadronicSUSY/MCResolutions/data/QCD_13TeV_madgraph_PHYS14'
process.QCDfromSmearing.BProbabilityFile = '/afs/naf.desy.de/user/k/kriheine/Resolution/BJetProbabilityMC.root'
process.QCDfromSmearing.jetCollection = InputJetTag
process.QCDfromSmearing.uncertaintyName = '' 
#process.QCDfromSmearing.InputHisto1_HF = 'h_tot_JetAll_ResponsePt'
#process.QCDfromSmearing.InputHisto2_HF = 'h_tot_JetAll_ResponsePt'
#process.QCDfromSmearing.InputHisto3p_HF = 'h_tot_JetAll_ResponsePt'
#process.QCDfromSmearing.InputHisto1_NoHF = 'h_tot_JetAll_ResponsePt'
#process.QCDfromSmearing.InputHisto2_NoHF = 'h_tot_JetAll_ResponsePt'
#process.QCDfromSmearing.InputHisto3p_NoHF = 'h_tot_JetAll_ResponsePt'
process.QCDfromSmearing.InputHisto1_HF = 'h_b_JetAll_ResponsePt'
process.QCDfromSmearing.InputHisto2_HF = 'h_b_JetAll_ResponsePt'
process.QCDfromSmearing.InputHisto3p_HF = 'h_b_JetAll_ResponsePt'
process.QCDfromSmearing.InputHisto1_NoHF = 'h_nob_JetAll_ResponsePt'
process.QCDfromSmearing.InputHisto2_NoHF = 'h_nob_JetAll_ResponsePt'
process.QCDfromSmearing.InputHisto3p_NoHF = 'h_nob_JetAll_ResponsePt'
process.QCDfromSmearing.RebalanceCorrectionFile = '/afs/naf.desy.de/user/k/kriheine/Resolution/RebalanceCorrection_DR53X_withoutPUReweighting_pt10.root'
process.QCDfromSmearing.NRebin = 1
process.QCDfromSmearing.NJets = 2
process.QCDfromSmearing.SmearCollection = 'Reco'
process.QCDfromSmearing.PtBinEdges_scaling = cms.vdouble(0., 7000.)
process.QCDfromSmearing.EtaBinEdges_scaling = cms.vdouble(0.0, 5.0)
process.QCDfromSmearing.AdditionalSmearing = cms.vdouble(1.0)
process.QCDfromSmearing.LowerTailScaling = cms.vdouble(1.0)
process.QCDfromSmearing.UpperTailScaling = cms.vdouble(1.0)
process.QCDfromSmearing.SmearedJetPt = 0.
process.QCDfromSmearing.RebalanceJetPt = 10.
process.QCDfromSmearing.RebalanceMode = 'MHThigh'
process.QCDfromSmearing.weightName = 'WeightProducer:weight:RA2QCDSmearingClosure'
process.QCDfromSmearing.ControlPlots = True
process.QCDfromSmearing.Ntries = 100
process.QCDfromSmearing.cleverPrescaleTreating = False
process.QCDfromSmearing.useRebalanceCorrectionFactors = False
process.QCDfromSmearing.MHTcut_low = cms.double(200.)
process.QCDfromSmearing.MHTcut_medium = cms.double(350.)
process.QCDfromSmearing.MHTcut_high = cms.double(500.)
process.QCDfromSmearing.HTcut_low = cms.double(500.)
process.QCDfromSmearing.HTcut_medium = cms.double(800.)
process.QCDfromSmearing.HTcut_high = cms.double(1000.)
process.QCDfromSmearing.HTcut_veryhigh = cms.double(1200.)
process.QCDfromSmearing.HTcut_extremehigh = cms.double(1400.)
###############################################################################

###############################################################################
## --- Setup of TreeMaker ----------------------------------------------
from RA2Classic.TreeMaker.treemaker_cfi import TreeMaker
process.RA2TreeMaker = TreeMaker.clone(
    TreeName         = cms.string("RA2PreSelection"),
    VarsDouble       = cms.VInputTag(cms.InputTag('weightProducer:weight')),
    VarsDoubleNamesInTree = cms.vstring('Weight'),
    VertexCollection = cms.InputTag('goodVertices'),
    HT               = cms.InputTag('htPFchs'),
    HTJets           = cms.InputTag('HTJets'),
    MHT              = cms.InputTag('mhtPFchs'),
    MHTJets          = cms.InputTag('MHTJets')
    )
process.load('RA2Classic.Utils.produceRA2JetsPFCHS_cff')
#process.load('RA2Classic.Utils.produceRA2JetsAK5PF_cff')
###############################################################################

###############################################################################
process.dump   = cms.EDAnalyzer("EventContentAnalyzer")
###############################################################################

process.prediction = cms.Path(
#	process.dump *
   process.RA2_HBHENoiseFilterRA2 *
   process.RA2_beamHaloFilter *
   #process.RA2_eeNoiseFilter *
   process.RA2_trackingFailureFilter *
   process.RA2_inconsistentMuons *
   process.RA2_greedyMuons *
   process.RA2_EcalTPFilter *
   process.RA2_EcalBEFilter *
   process.HCALLaserEvtFilterList2012 *
   #process.HcalLaserEventFilter *
   process.EcalLaserFilter *
   process.EEBadScFilter *
   ~process.manyStripClustersFilter *
   ~process.tooManyStripClustersFilter *
   ~process.logErrorTooManyClustersFilter *
	process.weightProducer *
   process.PBNRFilter *
   process.ra2PFMuonVeto *
   process.ra2ElectronVeto *
	process.QCDfromSmearing 
)

process.mc = cms.Path(
   process.RA2_HBHENoiseFilterRA2 *
   process.RA2_beamHaloFilter *
   #process.RA2_eeNoiseFilter *
   process.RA2_trackingFailureFilter *
   process.RA2_inconsistentMuons *
   process.RA2_greedyMuons *
   process.RA2_EcalTPFilter *
   process.RA2_EcalBEFilter *
   process.HCALLaserEvtFilterList2012 *
   #process.HcalLaserEventFilter *
   process.EcalLaserFilter *
   process.EEBadScFilter *
   ~process.manyStripClustersFilter *
   ~process.tooManyStripClustersFilter *
   ~process.logErrorTooManyClustersFilter *
	process.weightProducer *
   process.PBNRFilter *
   process.ra2PFMuonVeto *
   process.ra2ElectronVeto * 
   process.produceRA2JetsPFCHS *
   process.RA2TreeMaker   
)
