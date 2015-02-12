import FWCore.ParameterSet.Config as cms

process = cms.Process("RA2QCDSmearingClosure")

###############################################################################
#-- Message Logger ------------------------------------------------------------
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.suppressWarning = cms.untracked.vstring('TriggerSelectionLow','TriggerSelectionHigh','TriggerSelectionSignal')
 
###############################################################################

## Options and Output Report
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
           '/store/user/mschrode/HT/RA2PreSelection_Run2012A-13Jul2012-v1_V2/528d417548fa47de754292e17c1b0d17/RA2Skim_215_1_7bE.root',
           '/store/user/mschrode/HT/RA2PreSelection_Run2012A-13Jul2012-v1_V2/528d417548fa47de754292e17c1b0d17/RA2Skim_28_1_EOW.root',
           '/store/user/mschrode/HT/RA2PreSelection_Run2012A-13Jul2012-v1_V2/528d417548fa47de754292e17c1b0d17/RA2Skim_215_1_7bE.root',
           '/store/user/mschrode/HT/RA2PreSelection_Run2012A-13Jul2012-v1_V2/528d417548fa47de754292e17c1b0d17/RA2Skim_27_1_LQC.root',
           '/store/user/mschrode/HT/RA2PreSelection_Run2012A-13Jul2012-v1_V2/528d417548fa47de754292e17c1b0d17/RA2Skim_32_1_HnL.root',
           '/store/user/mschrode/HT/RA2PreSelection_Run2012A-13Jul2012-v1_V2/528d417548fa47de754292e17c1b0d17/RA2Skim_47_1_Q7T.root',
           '/store/user/mschrode/HT/RA2PreSelection_Run2012A-13Jul2012-v1_V2/528d417548fa47de754292e17c1b0d17/RA2Skim_72_1_DcZ.root',
           '/store/user/mschrode/HT/RA2PreSelection_Run2012A-13Jul2012-v1_V2/528d417548fa47de754292e17c1b0d17/RA2Skim_82_1_zkG.root'
	)
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( 1000 ) )

###############################################################################
## Global tags and geometry
# default configuration with frontier conditions
#process.load("Configuration.Geometry.GeometryIdeal_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.GlobalTag.globaltag = cms.string('FT_53_V6_AN2::All')
###############################################################################

###############################################################################
process.TFileService = cms.Service("TFileService",fileName = cms.string("Selection_OnData_2012.root") )
###############################################################################

###############################################################################
# Filters
###############################################################################
from RecoMET.METFilters.jetIDFailureFilter_cfi import jetIDFailure
process.PBNRFilter = jetIDFailure.clone(
    JetSource = cms.InputTag('patJetsPF'),
    MinJetPt      = cms.double(30.0),
    taggingMode   = cms.bool(False)
    )
from RecoMET.METFilters.multiEventFilter_cfi import multiEventFilter
process.HCALLaserEvtFilterList2012 = multiEventFilter.clone(
    file        = cms.FileInPath('EventFilter/HcalRawToDigi/data/AllBadHCALLaser.txt'),
    taggingMode = cms.bool(False)
    )

process.load("SandBox.Skims.filterBoolean_cfi")
process.RA2_HBHENoiseFilterRA2    = process.booleanFilter.clone()
process.RA2_HBHENoiseFilterRA2.ResultSource = cms.InputTag("HBHENoiseFilterRA2","HBHENoiseFilterResult","PAT")
process.RA2_beamHaloFilter        = process.booleanFilter.clone()
process.RA2_beamHaloFilter.ResultSource = cms.InputTag("beamHaloFilter")
process.RA2_eeNoiseFilter         = process.booleanFilter.clone()
process.RA2_eeNoiseFilter.ResultSource = cms.InputTag("eeNoiseFilter")
process.RA2_trackingFailureFilter = process.booleanFilter.clone()
process.RA2_trackingFailureFilter.ResultSource = cms.InputTag("trackingFailureFilter")
process.RA2_inconsistentMuons     = process.booleanFilter.clone()
process.RA2_inconsistentMuons.ResultSource = cms.InputTag("inconsistentMuons")
process.RA2_greedyMuons           = process.booleanFilter.clone()
process.RA2_greedyMuons.ResultSource = cms.InputTag("greedyMuons")
process.RA2_EcalTPFilter          = process.booleanFilter.clone()
process.RA2_EcalTPFilter.ResultSource = cms.InputTag("ra2EcalTPFilter")
process.RA2_EcalBEFilter          = process.booleanFilter.clone()
process.RA2_EcalBEFilter.ResultSource = cms.InputTag("ra2EcalBEFilter")
#process.HcalLaserEventFilter      = process.booleanFilter.clone()
#process.HcalLaserEventFilter.ResultSource = cms.InputTag("hcalLaserEventFilter")
process.EEBadScFilter             = process.booleanFilter.clone()
process.EEBadScFilter.ResultSource = cms.InputTag("eeBadScFilter")
#process.EcalLaserFilter           = process.booleanFilter.clone()
#process.EcalLaserFilter.ResultSource= cms.InputTag("ecalLaserCorrFilter")
###############################################################################

###############################################################################
# Lepton Veto
###############################################################################
process.load('SandBox.Skims.RA2Leptons_cff')
###############################################################################

###############################################################################
## --- Setup of TreeMaker ----------------------------------------------
from RA2Classic.TreeMaker.treemaker_cfi import TreeMaker
process.RA2TreeMaker = TreeMaker.clone(
    TreeName         = cms.string("RA2PreSelection"),
    VarsDouble       = cms.VInputTag(cms.InputTag('weightProducer:weight')),
    VarsDoubleNamesInTree = cms.vstring('Weight'),
    VertexCollection = cms.InputTag('goodVertices'),
 #   HT               = cms.InputTag('htPF'),
    HT               = cms.InputTag('htPFchs'),
    HTJets           = cms.InputTag('HTJets'),
 #   MHT              = cms.InputTag('mhtPF'),
    MHT              = cms.InputTag('mhtPFchs'),
    MHTJets          = cms.InputTag('MHTJets')
    )
process.load('RA2Classic.Utils.produceRA2JetsPFCHS_cff')
#process.load('RA2Classic.Utils.produceRA2JetsAK5PF_cff')
###############################################################################

###############################################################################
# HLThltEventAnalyzer
###############################################################################
process.load("HLTrigger.HLTcore.hltEventAnalyzerAOD_cfi")
###############################################################################

process.dump   = cms.EDAnalyzer("EventContentAnalyzer")

process.data = cms.Path(
   process.RA2_HBHENoiseFilterRA2 *
   process.RA2_beamHaloFilter *
#   process.RA2_eeNoiseFilter *
   process.RA2_trackingFailureFilter *
   process.RA2_inconsistentMuons *
   process.RA2_greedyMuons *
   process.RA2_EcalTPFilter *
   process.RA2_EcalBEFilter *
   process.EEBadScFilter *
   process.HCALLaserEvtFilterList2012 *
   process.PBNRFilter *
   process.ra2PFMuonVeto *
   process.ra2ElectronVeto * 
   process.produceRA2JetsPFCHS *
 #  process.produceRA2JetsAK5PF *
   process.RA2TreeMaker   
)

