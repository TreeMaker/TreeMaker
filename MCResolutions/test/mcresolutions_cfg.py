# Expects a file name as argument e.g.
# cmsRun mcresolutions_cfg.py data_set=/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM, global_tag=PHYS14_25_V1

## --- Read parameters --------------------------------------------------
from TreeMaker.Utils.CommandLineParams import CommandLineParams
parameters = CommandLineParams()

runOnMC = parameters.value("is_mc",True)
dataSetName = parameters.value("data_set","/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM")
testFileName = parameters.value("test_file_name","/store/mc/Phys14DR/QCD_HT-500To1000_13TeV-madgraph/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/481A6155-916F-E411-BA52-00266CFFCAF0.root")
globalTag = parameters.value("global_tag","PHYS14_25_V1")+"::All"
lumi = parameters.value("lumi",10000.0)
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
from TreeMaker.WeightProducer.getWeightProducer_cff import getWeightProducer
process.WeightProducer = getWeightProducer(dataSetName)
process.WeightProducer.Lumi = cms.double(lumi)
process.WeightProducer.PU = cms.int32(0) # PU: 3 for S10, 2 for S7
process.WeightProducer.FileNamePUDataDistribution = cms.string("NONE")

## --- isotrack producer -----------------------------------------------
from TreeMaker.Utils.trackIsolationMaker_cfi import trackIsolationFilter
process.IsolatedElectronTracksVeto = trackIsolationFilter.clone(
                                                                doTrkIsoVeto= True,
                                                                vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                                                pfCandidatesTag = cms.InputTag("packedPFCandidates"),
                                                                dR_ConeSize = cms.double(0.3),
                                                                dz_CutValue = cms.double(0.05),
                                                                minPt_PFCandidate = cms.double(5.0),
                                                                isoCut = cms.double(0.2),
                                                                pdgId = cms.int32(11),
                                                                mTCut = cms.double(100.),
                                                                )
   
process.IsolatedMuonTracksVeto = trackIsolationFilter.clone(
                                                            doTrkIsoVeto= True,
                                                            vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                                            pfCandidatesTag = cms.InputTag("packedPFCandidates"),
                                                            dR_ConeSize = cms.double(0.3),
                                                            dz_CutValue = cms.double(0.05),
                                                            minPt_PFCandidate = cms.double(5.0),
                                                            isoCut = cms.double(0.2),
                                                            pdgId = cms.int32(13),
                                                            mTCut = cms.double(100.),
                                                            )
      
process.IsolatedPionTracksVeto = trackIsolationFilter.clone(
                                                            doTrkIsoVeto= True,
                                                            vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                                            pfCandidatesTag = cms.InputTag("packedPFCandidates"),
                                                            dR_ConeSize = cms.double(0.3),
                                                            dz_CutValue = cms.double(0.05),
                                                            minPt_PFCandidate = cms.double(10.0),
                                                            isoCut = cms.double(0.1),
                                                            pdgId = cms.int32(211),
                                                            mTCut = cms.double(100.),
                                                            )

## --- good leptons producer -------------------------------------------
from TreeMaker.Utils.leptonproducer_cfi import leptonproducer
process.GoodLeptons = leptonproducer.clone(
                                           MuonTag = cms.InputTag('slimmedMuons'),
                                           ElectronTag = cms.InputTag('slimmedElectrons'),
                                           PrimaryVertex = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                           minElecPt = cms.double(10),
                                           maxElecEta = cms.double(2.5),
                                           minMuPt = cms.double(10),
                                           maxMuEta = cms.double(2.4),
                                           UseMiniIsolation = cms.bool(True),
                                           muIsoValue = cms.double(0.2),
                                           elecIsoValue = cms.double(0.1), # only has an effect when used with miniIsolation
                                           METTag = cms.InputTag('slimmedMETs'),
                                           )

## --- good photon producer -----------------------------------------------
process.GoodPhotons = cms.EDProducer("PhotonIDisoProducer",
                                     photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                     rhoCollection = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
                                     debug = cms.untracked.bool(False)
                                     )

## --- good jets producer -----------------------------------------------
from TreeMaker.Utils.goodjetsproducer_cfi import GoodJetsProducer
process.GoodJets = GoodJetsProducer.clone(
                                          TagMode = cms.bool(False),
                                          JetTag= cms.InputTag('slimmedJets'),
                                          #JetTag= cms.InputTag('patJetsReapplyJEC'),
                                          maxJetEta = cms.double(5.0),
                                          maxMuFraction = cms.double(2),
                                          minNConstituents = cms.double(2),
                                          maxNeutralFraction = cms.double(0.90),
                                          maxPhotonFraction = cms.double(0.95),
                                          minChargedMultiplicity = cms.double(0),
                                          minChargedFraction = cms.double(0),
                                          maxChargedEMFraction = cms.double(0.99),
                                          jetPtFilter = cms.double(30),
                                          ExcludeLepIsoTrackPhotons = cms.bool(True),
                                          JetConeSize = cms.double(0.04),
                                          MuonTag = cms.InputTag('GoodLeptons:IdIsoMuon'),
                                          ElecTag = cms.InputTag('GoodLeptons:IdIsoElectron'),
                                          IsoElectronTrackTag = cms.InputTag('IsolatedElectronTracksVeto'),
                                          IsoMuonTrackTag = cms.InputTag('IsolatedMuonTracksVeto'),
                                          IsoPionTrackTag = cms.InputTag('IsolatedPionTracksVeto'),
                                          PhotonTag = cms.InputTag('GoodPhotons','bestPhoton'),
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
from TreeMaker.MCResolutions.mcresolutions_cfi import MCResolutions
process.MCReso = MCResolutions.clone()
process.MCReso.jetTag = mcResoJetTag
process.MCReso.fileName = mcResoFileName
process.MCReso.leptonTag = mcResoLeptonTag

## --- Setup dump event content ----------------------------------------
process.dump   = cms.EDAnalyzer("EventContentAnalyzer")

process.p = cms.Path(
                     process.IsolatedElectronTracksVeto *
                     process.IsolatedMuonTracksVeto *
                     process.IsolatedPionTracksVeto *
                     process.GoodLeptons *
                     process.GoodPhotons *
                     process.GoodJets *
                     process.WeightProducer *
                     #process.dump *
                     process.MCReso
                     )
