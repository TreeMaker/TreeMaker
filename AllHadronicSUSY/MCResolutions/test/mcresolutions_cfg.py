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
mcResoJetTag = parameters.value("jet_tag","GoodJets")
mcResoLeptonTag = parameters.value("lepton_tag","GoodLeptons")
mcResoFileName = parameters.value("out_name","MCResoDefault.root")

print "*** JOB SETUP ****************************************************"
print "  is_mc          : "+str(runOnMC)
print "  data_set       : "+dataSetName
print "  global_tag     : "+globalTag
print "  lumi           : "+str(lumi)
print "  pu_reweighting : "+str(doPUReweighting)
print "  jet_tag        : "+mcResoJetTag
print "  lepton_tag     : "+mcResoLeptonTag
print "  out_name       : "+mcResoFileName
print "******************************************************************"

## --- The process needs to be defined AFTER reading sys.argv, ---------
## --- otherwise edmConfigHash fails -----------------------------------
import FWCore.ParameterSet.Config as cms
process = cms.Process("ResponseTemplates")

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

## --- isotrack producer -----------------------------------------------
from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationFilter
process.IsolatedTracksVeto = trackIsolationFilter.clone(
                                                        doTrkIsoVeto= True,
                                                        vertexInputTag     = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                                        pfCandidatesTag    = cms.InputTag("packedPFCandidates"),
                                                        dR_ConeSize        = cms.double(0.3),
                                                        dz_CutValue        = cms.double(0.05),
                                                        minPt_PFCandidate  = cms.double(15.0),
                                                        isoCut             = cms.double(0.1),
                                                        mTCut              = cms.double(100.),
                                                        )

## --- god jets producer -----------------------------------------------
from AllHadronicSUSY.Utils.goodjetsproducer_cfi import GoodJetsProducer
process.GoodJets = GoodJetsProducer.clone(
                                          JetTag                  = cms.InputTag('slimmedJets'),
                                          maxJetEta               = cms.double(5.0),
                                          maxMuFraction           = cms.double(2),
                                          minNConstituents        = cms.double(2),
                                          maxNeutralFraction      = cms.double(0.99),
                                          maxPhotonFraction       = cms.double(0.99),
                                          minChargedMultiplicity  = cms.double(0),
                                          minChargedFraction      = cms.double(0),
                                          maxChargedEMFraction    = cms.double(0.99),
                                          )

## --- good leptons producer -------------------------------------------
from AllHadronicSUSY.Utils.leptonproducer_cfi import leptonproducer
process.GoodLeptons = leptonproducer.clone(
                                           MuonTag        = cms.InputTag('slimmedMuons'),
                                           ElectronTag    = cms.InputTag('slimmedElectrons'),
                                           PrimaryVertex  = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                           minElecPt      = cms.double(10),
                                           maxElecEta     = cms.double(2.5),
                                           minMuPt        = cms.double(10),
                                           maxMuEta       = cms.double(2.4),
                                           )

## --- MET filters -----------------------------------------------------
## We don't use "import *" because the cff contains some modules for which the C++ class doesn't exist
## and this triggers an error under unscheduled mode
from RecoMET.METFilters.metFilters_cff import HBHENoiseFilter, CSCTightHaloFilter, hcalLaserEventFilter, EcalDeadCellTriggerPrimitiveFilter, eeBadScFilter, ecalLaserCorrFilter
from RecoMET.METFilters.metFilters_cff import goodVertices, trackingFailureFilter, trkPOGFilters, manystripclus53X, toomanystripclus53X, logErrorTooManyClusters
from RecoMET.METFilters.metFilters_cff import metFilters

## individual filters
#Flag_HBHENoiseFilter = cms.Path(HBHENoiseFilter)
#Flag_CSCTightHaloFilter = cms.Path(CSCTightHaloFilter)
#Flag_hcalLaserEventFilter = cms.Path(hcalLaserEventFilter)
#Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(EcalDeadCellTriggerPrimitiveFilter)
#Flag_goodVertices = cms.Path(goodVertices)
#Flag_trackingFailureFilter = cms.Path(goodVertices + trackingFailureFilter)
#Flag_eeBadScFilter = cms.Path(eeBadScFilter)
#Flag_ecalLaserCorrFilter = cms.Path(ecalLaserCorrFilter)
#Flag_trkPOGFilters = cms.Path(trkPOGFilters)
## and the sub-filters
#Flag_trkPOG_manystripclus53X = cms.Path(~manystripclus53X)
#Flag_trkPOG_toomanystripclus53X = cms.Path(~toomanystripclus53X)
#Flag_trkPOG_logErrorTooManyClusters = cms.Path(~logErrorTooManyClusters)

#process.Filter_HBHENoiseFilter = HBHENoiseFilter.clone()

# and the summary
#Flag_METFilters = cms.Path(metFilters)

#def miniAOD_customizeMETFiltersFastSim(process):
#   """Replace some MET filters that don't work in FastSim with trivial bools"""
#   for X in 'CSCTightHaloFilter', 'HBHENoiseFilter':
#      process.globalReplace(X, cms.EDFilter("HLTBool", result=cms.bool(True)))
#   for X in 'manystripclus53X', 'toomanystripclus53X', 'logErrorTooManyClusters':
#      process.globalReplace(X, cms.EDFilter("HLTBool", result=cms.bool(False)))
#   return process

## --- Setup MC Truth templates writer ---------------------------------
from AllHadronicSUSY.MCResolutions.mcresolutions_cfi import MCResolutions
process.MCReso = MCResolutions.clone()
process.MCReso.jetTag = mcResoJetTag
process.MCReso.fileName = mcResoFileName
process.MCReso.leptonTag = mcResoLeptonTag

## --- Setup dump event content ----------------------------------------
process.dump   = cms.EDAnalyzer("EventContentAnalyzer")

process.p = cms.Path(
                     process.IsolatedTracksVeto *
                     process.GoodJets *
                     process.GoodLeptons *
                     process.WeightProducer *
                     #process.dump *
                     process.MCReso
                     )
