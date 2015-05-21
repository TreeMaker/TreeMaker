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
InputJetTag = parameters.value("jet_tag","GoodJets")
InputLeptonTag = parameters.value("lepton_tag","GoodLeptons")
OutputFileName = parameters.value("out_name","QCDSmearingClosure_OnMC.root")

print "*** JOB SETUP ****************************************************"
print "  is_mc          : "+str(runOnMC)
print "  data_set       : "+dataSetName
print "  global_tag     : "+globalTag
print "  lumi           : "+str(lumi)
print "  pu_reweighting : "+str(doPUReweighting)
print "  jet_tag        : "+InputJetTag
print "  lepton_tag     : "+InputLeptonTag
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
process.MessageLogger.cout = cms.untracked.PSet(INFO = cms.untracked.PSet(reportEvery = cms.untracked.int32(100)))
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

## --- Input Source ----------------------------------------------------
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source("PoolSource",fileNames = cms.untracked.vstring(testFileName))
process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

## --- Setup WeightProducer --------------------------------------------
print "*** WeightProducer setup **************************************************"
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
print "*** R+S Configuration **************************************************"
process.QCDfromSmearing.SmearingFile = '/afs/desy.de/user/c/csander/xxl-af-cms/CMSSW_7_2_3_patch1/src/AllHadronicSUSY/MCResolutions/data/QCD_13TeV_madgraph_PHYS14_v2.root'
process.QCDfromSmearing.jetCollection = InputJetTag
process.QCDfromSmearing.leptonTag = InputLeptonTag
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
process.QCDfromSmearing.RebalanceCorrectionFile = '/nfs/dust/cms/user/csander/RA2/AdditionalInputFiles_8TeV/RebalanceCorrection_DR53X_withoutPUReweighting_pt10.root'
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

VarsInt = cms.vstring()
VarsDouble = cms.vstring()
RecoCandVector = cms.vstring()

# baseline producers
process.Baseline = cms.Sequence(
)

## --- NVertex producer -----------------------------------------------
print "*** NVertex producer **************************************************"
from AllHadronicSUSY.Utils.primaryverticies_cfi import primaryverticies
process.NVtx = primaryverticies.clone(
                                      VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                      )
process.Baseline += process.NVtx
VarsInt.extend(['NVtx'])

## --- isotrack producer -----------------------------------------------
print "*** isotrack producer **************************************************"
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
process.Baseline += process.IsolatedTracksVeto

## --- god jets producer -----------------------------------------------
print "*** good jets producer **************************************************"
from AllHadronicSUSY.Utils.goodjetsproducer_cfi import GoodJetsProducer
process.GoodJets = GoodJetsProducer.clone(
                                          JetTag                  = cms.InputTag('slimmedJets'),
                                          maxMuFraction           = cms.double(2),
                                          minNConstituents        = cms.double(1),
                                          maxNeutralFraction      = cms.double(0.99),
                                          maxPhotonFraction       = cms.double(0.99),
                                          minChargedMultiplicity  = cms.double(0),
                                          minChargedFraction      = cms.double(0),
                                          maxChargedEMFraction    = cms.double(0.99),
)
process.Baseline += process.GoodJets

## --- good leptons producer -------------------------------------------
print "*** good leptons producer **************************************************"
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
process.Baseline += process.GoodLeptons

## --- HT jets producer ------------------------------------------------
print "*** HT jets producer **************************************************"
from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
process.HTJets = SubJetSelection.clone(
                                       JetTag   = cms.InputTag('GoodJets'),
                                       MinPt    = cms.double(30),
                                       MaxEta   = cms.double(2.4),
)
process.Baseline += process.HTJets

## --- HT producer -----------------------------------------------------
print "*** HT producer **************************************************"
from AllHadronicSUSY.Utils.htdouble_cfi import htdouble
process.HT = htdouble.clone(
                            JetTag  = cms.InputTag('HTJets'),
)
process.Baseline += process.HT
VarsDouble.extend(['HT'])
   
## --- NJets producer --------------------------------------------------
print "*** NJets producer **************************************************"
from AllHadronicSUSY.Utils.njetint_cfi import njetint
process.NJets = njetint.clone(
                              JetTag  = cms.InputTag('HTJets'),
)
process.Baseline += process.NJets
VarsInt.extend(['NJets'])

## --- NBJets producer -------------------------------------------------
print "*** NBJets producer **************************************************"
from AllHadronicSUSY.Utils.btagint_cfi import btagint
process.BTags = btagint.clone(
                              JetTag         = cms.InputTag('HTJets'),
                              BTagInputTag   = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
                              BTagCutValue   = cms.double(0.814)
)
process.Baseline += process.BTags
VarsInt.extend(['BTags'])

## --- MHT jets producer -----------------------------------------------
print "*** MHT jets producer **************************************************"
from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
process.MHTJets = SubJetSelection.clone(
                                        JetTag  = cms.InputTag('GoodJets'),
                                        MinPt   = cms.double(30),
                                        MaxEta  = cms.double(5.0),
                                        )
process.Baseline += process.MHTJets

## --- MHT producer ----------------------------------------------------
print "*** MHT producer **************************************************"
from AllHadronicSUSY.Utils.mhtdouble_cfi import mhtdouble
process.MHT = mhtdouble.clone(
                              JetTag  = cms.InputTag('MHTJets'),
)
process.Baseline += process.MHT
VarsDouble.extend(['MHT'])

## --- DeltaPhi producer -----------------------------------------------
print "*** DeltaPhi producer **************************************************"
from AllHadronicSUSY.Utils.deltaphidouble_cfi import deltaphidouble
process.DeltaPhi = deltaphidouble.clone(
                                        DeltaPhiJets  = cms.InputTag('HTJets'),
                                        MHTJets       = cms.InputTag("MHTJets"),
)
process.Baseline += process.DeltaPhi
VarsDouble.extend(['DeltaPhi:Jet1Pt','DeltaPhi:Jet2Pt','DeltaPhi:Jet3Pt'])
VarsDouble.extend(['DeltaPhi:Jet1Eta','DeltaPhi:Jet2Eta','DeltaPhi:Jet3Eta'])
VarsDouble.extend(['DeltaPhi:DeltaPhi1','DeltaPhi:DeltaPhi2','DeltaPhi:DeltaPhi3'])

## --- DeltaPhiN producer ----------------------------------------------
#print "*** DeltaPhiN producer **************************************************"
#from AllHadronicSUSY.Utils.metdouble_cfi import metdouble
#process.MET = metdouble.clone(
#                              METTag  = cms.InputTag("slimmedMETs"),
#                              JetTag  = cms.InputTag('HTJets'),
#)
#process.Baseline += process.MET
#VarsDouble.extend(['MET:minDeltaPhiN','MET:DeltaPhiN1','MET:DeltaPhiN2','MET:DeltaPhiN3','MET:Pt(METPt)','MET:Phi(METPhi)'])

## --- Setup of TreeMaker ----------------------------------------------

VarsDouble.extend(['WeightProducer:weight(Weight)'])

print "*** Treemaker setup **************************************************"
from AllHadronicSUSY.TreeMaker.treeMaker import TreeMaker
process.RA2TreeMaker = TreeMaker.clone(
                                       TreeName       = cms.string("PreSelection"),
                                       VarsRecoCand   = RecoCandVector,
                                       VarsDouble     = VarsDouble,
                                       VarsInt        = VarsInt,
)
###############################################################################

###############################################################################
process.dump   = cms.EDAnalyzer("EventContentAnalyzer")
###############################################################################

process.prediction = cms.Path(
                              process.Baseline *
                              process.WeightProducer *
                              process.QCDfromSmearing
                              #* process.dump
)

process.mc = cms.Path(
                      process.WeightProducer *
                      process.Baseline *
                      process.RA2TreeMaker
                      #* process.dump
)
