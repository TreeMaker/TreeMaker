# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms
import sys,os
def makeTreeFromMiniAOD(
process,
outFileName,
reportEveryEvt=10,
testFileName="",
Global_Tag="",
numProcessedEvt=1000,
lostlepton=False,
tagandprobe=False,
applybaseline=False,
doZinv=False,
debugtracks=False,
geninfo=True,
filtertag="PAT",
jsonfile=""
):

    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
    process.GlobalTag.globaltag = Global_Tag
    
    # define if mt cut should be applied and the value (less than 0 means no cut)
    mtcut = cms.double(100)
    if tagandprobe:
      mtcut=-100
      print "Doing tagandprobe"
    print "Calulation with mtcut: "+ str(mtcut)

    ## --- Log output ------------------------------------------------------
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.cerr.FwkReport.reportEvery = reportEveryEvt
    process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True)
        )

    ## --- Files to process ------------------------------------------------
    import FWCore.PythonUtilities.LumiList as LumiList
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(numProcessedEvt)
        )
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(testFileName)
    )
    if len(jsonfile)>0: process.source.lumisToProcess = LumiList.LumiList(filename = jsonfile).getVLuminosityBlockRange()

    ## --- Output file -----------------------------------------------------
    process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string(outFileName+".root")
        )
    # config of producers
    RecoCandVector = cms.vstring() 
    VarsDouble = cms.vstring()
    VarsInt = cms.vstring()
    VarsBool = cms.vstring()
    VectorTLorentzVector = cms.vstring()
    VectorDouble = cms.vstring()
    VectorString = cms.vstring()
    VectorInt = cms.vstring()
    # baseline producers
    process.Baseline = cms.Sequence(
    )
    #special sequences
    #lost-lepton variables
    process.LostLepton = cms.Sequence(
      
    )

    # configure treemaker
    from AllHadronicSUSY.TreeMaker.treeMaker import TreeMaker
    process.TreeMaker2 = TreeMaker.clone(
    	TreeName          = cms.string("PreSelection"),
    	VarsRecoCand = RecoCandVector, 
    	VarsDouble  	  = VarsDouble,
    	VarsInt = VarsInt,
    	VarsBool = VarsBool,
        VectorTLorentzVector = VectorTLorentzVector,
        VectorDouble = VectorDouble,
        VectorInt = VectorInt,
        VectorString = VectorString,
    	)

    # basic producers
    ## --- Setup WeightProducer -------------------------------------------
    from AllHadronicSUSY.WeightProducer.getWeightProducer_cff import getWeightProducer
    process.WeightProducer = getWeightProducer(testFileName)
    process.WeightProducer.Lumi                       = cms.double(4000)
    process.WeightProducer.PU                         = cms.int32(0) # PU S10 3 for S10 2 for S7
    process.WeightProducer.FileNamePUDataDistribution = cms.string("NONE")
    print process.WeightProducer.PU
    process.Baseline += process.WeightProducer
    VarsDouble.extend(['WeightProducer:weight(Weight)'])
    from AllHadronicSUSY.Utils.primaryvertices_cfi import primaryvertices
    process.NVtx = primaryvertices.clone(
    VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    )
    process.Baseline += process.NVtx
    VarsInt.extend(['NVtx'])

    ###############
    # gen stuff
    ###############
    
    if geninfo :
        process.genParticles = cms.EDProducer("genParticlesProducer",
                                              genCollection = cms.untracked.InputTag("prunedGenParticles"),
                                              debug = cms.untracked.bool(False)
                                              )
    
        VectorTLorentzVector.append("genParticles(genParticles)")
        VectorInt.append("genParticles:PDGid(genParticles_PDGid)")
        #VectorInt.append("genParticles:parent(genParticles_parent)")
    
        process.Baseline += process.genParticles

    ## isotrack producer
    from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationFilter
    from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationCounter
    
    process.IsolatedElectronTracksVeto = trackIsolationFilter.clone(
      doTrkIsoVeto= False,
      vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
      pfCandidatesTag = cms.InputTag("packedPFCandidates"),
      dR_ConeSize         = cms.double(0.3),
      dz_CutValue         = cms.double(0.1),
      minPt_PFCandidate   = cms.double(5.0),
      isoCut              = cms.double(0.2),
      pdgId               = cms.int32(11),
      mTCut=mtcut,
      )

    process.IsolatedMuonTracksVeto = trackIsolationFilter.clone(
      doTrkIsoVeto= False,
      vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
      pfCandidatesTag = cms.InputTag("packedPFCandidates"),
      dR_ConeSize         = cms.double(0.3),
      dz_CutValue         = cms.double(0.1),
      minPt_PFCandidate   = cms.double(5.0),
      isoCut              = cms.double(0.2), 
      pdgId               = cms.int32(13),
      mTCut=mtcut,
      )

    process.IsolatedPionTracksVeto = trackIsolationFilter.clone(
      doTrkIsoVeto= False,
      vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
      pfCandidatesTag = cms.InputTag("packedPFCandidates"),
      dR_ConeSize         = cms.double(0.3),
      dz_CutValue         = cms.double(0.1),
      minPt_PFCandidate   = cms.double(10.0),
      isoCut              = cms.double(0.1),
      pdgId               = cms.int32(211),
      mTCut=mtcut,
      )

    process.Baseline += process.IsolatedElectronTracksVeto
    process.Baseline += process.IsolatedMuonTracksVeto
    process.Baseline += process.IsolatedPionTracksVeto

    VarsInt.extend(['IsolatedElectronTracksVeto:isoTracks(isoElectronTracks)'])
    VarsInt.extend(['IsolatedMuonTracksVeto:isoTracks(isoMuonTracks)'])
    VarsInt.extend(['IsolatedPionTracksVeto:isoTracks(isoPionTracks)'])

    #NB: this increases the runtime and size of ntuples by 10x
    #do not turn on unless you really want to save all the isotrack quantities!!!
    if debugtracks:
        #just store the full set of isotrack quantities once
        process.IsolatedPionTracksVeto.debug = cms.bool(True)
        VarsBool.extend(['IsolatedPionTracksVeto:GoodVtx(GoodVtx)'])
        VectorTLorentzVector.extend(['IsolatedPionTracksVeto:pfcands(pfcands)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandstrkiso(pfcands_trkiso)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsdzpv(pfcands_dzpv)'])
        VectorDouble.extend(['IsolatedPionTracksVeto:pfcandsmT(pfcands_mT)'])
        VectorInt.extend(['IsolatedPionTracksVeto:pfcandschg(pfcands_chg)'])
        VectorInt.extend(['IsolatedPionTracksVeto:pfcandsid(pfcands_id)'])
    
    #done with isolated track vetos stuff
    ########################################################
    
    from AllHadronicSUSY.Utils.leptonproducer_cfi import leptonproducer
    process.LeptonsNew = leptonproducer.clone(
      MuonTag = cms.InputTag('slimmedMuons'),
      ElectronTag = cms.InputTag('slimmedElectrons'),
      PrimaryVertex = cms.InputTag('offlineSlimmedPrimaryVertices'),
      minElecPt								  = cms.double(10),
      maxElecEta								  = cms.double(2.5),
      minMuPt								  = cms.double(10),
      maxMuEta								  = cms.double(2.4),
      UseMiniIsolation = cms.bool(True),
      muIsoValue								  = cms.double(0.2),
      elecIsoValue								  = cms.double(0.1), # only has an effect when used with miniIsolation
      METTag = cms.InputTag('slimmedMETs'), 
      )
    process.Baseline += process.LeptonsNew
    VarsInt.extend(['LeptonsNew(Leptons)'])
    process.LeptonsNewTag = leptonproducer.clone(
      MuonTag = cms.InputTag('slimmedMuons'),
      ElectronTag = cms.InputTag('slimmedElectrons'),
      PrimaryVertex = cms.InputTag('offlineSlimmedPrimaryVertices'),
      minElecPt								  = cms.double(20),
      maxElecEta								  = cms.double(2.5),
      minMuPt								  = cms.double(20),
      maxMuEta								  = cms.double(2.4),
      muIsoValue								  = cms.double(0.2),
      elecIsoValue								  = cms.double(0.1), # only has an effect when used with miniIsolation
      UseMiniIsolation = cms.bool(True),
      METTag = cms.InputTag('slimmedMETs'), 
      )
    process.Baseline += process.LeptonsNewTag
    VarsInt.extend(['LeptonsNewTag(TagLeptonHighPT)'])

    ####### good photons
    process.goodPhotons = cms.EDProducer("PhotonIDisoProducer",
                                         photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                         electronCollection = cms.untracked.InputTag("slimmedElectrons"),
                                         conversionCollection = cms.untracked.InputTag("reducedEgamma","reducedConversions",filtertag),
                                         beamspotCollection = cms.untracked.InputTag("offlineBeamSpot","","RECO"),
                                         ecalRecHitsInputTag_EE = cms.InputTag("reducedEgamma","reducedEERecHits"),
                                         ecalRecHitsInputTag_EB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
                                         rhoCollection = cms.untracked.InputTag("fixedGridRhoFastjetAll"), 
                                         debug = cms.untracked.bool(False)
                                         )

    process.bestPhoton4Vec = cms.EDProducer("fourVectorProducer",
                                            particleCollection = cms.untracked.InputTag("goodPhotons","bestPhoton"),
                                            debug = cms.untracked.bool(False)
                                            )

    process.Baseline += process.goodPhotons
    process.Baseline += process.bestPhoton4Vec

    process.TreeMaker2.VectorTLorentzVector.append("bestPhoton4Vec(bestPhoton)")
    process.TreeMaker2.VarsInt.append("goodPhotons:NumPhotons(NumPhotons)")
    ######  done with photons -- good photon tag is InputTag('goodPhotons','bestPhoton')
    #################################

    ####### good jets -- the start of everything   
    JECPatch = cms.string('sqlite_file:PHYS14_V4_MC.db')
    #if gridcontrol: 
    if os.getenv('GC_CONF'): 
      JECPatch = cms.string('sqlite_file:../src/PHYS14_V4_MC.db')

    ####### JECs
    # get the JECs
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
######
    #from CondCore.DBCommon.CondDBSetup_cfi import *
    #process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
                               ##connect = cms.string('sqlite_file:../src/PHYS14_V4_MC.db'),
                               #connect = JECPatch,
                               ##connect = cms.string('AllHadronicSUSY/TreeMaker/test/PHYS14_V4_MC.db'),
                               #toGet = cms.VPSet(
            #cms.PSet(record = cms.string("JetCorrectionsRecord"),
                     #tag = cms.string("JetCorrectorParametersCollection_PHYS14_V4_MC_AK4PFchs"),
                     #label= cms.untracked.string("AK4PFchs")
                     #)
            #)
                               #)
    #process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")
    
    #from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetCorrFactorsUpdated
    #process.patJetCorrFactorsReapplyJEC = patJetCorrFactorsUpdated.clone(
        #src = cms.InputTag("slimmedJets"),
        #levels = ['L1FastJet', 
                  #'L2Relative', 
                  #'L3Absolute'],
        #payload = 'AK4PFchs' ) # Make sure to choose the appropriate levels and payload here!
    
    #from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetsUpdated
    #process.patJetsReapplyJEC = patJetsUpdated.clone(
        #jetSource = cms.InputTag("slimmedJets"),
        #jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
        #)
########

    ###### THIS IS JUST TEMPORARY, THESE SHOULD BE INCLUDED!!!!
    #process.Baseline += process.patJetCorrFactorsReapplyJEC
    #process.Baseline += process.patJetsReapplyJEC

    ############
    from AllHadronicSUSY.Utils.goodjetsproducer_cfi import GoodJetsProducer
    process.GoodJets = GoodJetsProducer.clone(
      TagMode = cms.bool(True),
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
      MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon'),
      ElecTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
      IsoElectronTrackTag = cms.InputTag('IsolatedElectronTracksVeto'),
      IsoMuonTrackTag = cms.InputTag('IsolatedMuonTracksVeto'),
      IsoPionTrackTag = cms.InputTag('IsolatedPionTracksVeto'),
      PhotonTag = cms.InputTag('goodPhotons','bestPhoton'),
      )
    process.Baseline += process.GoodJets
    VarsBool.extend(['GoodJets(JetID)'])
    #### done with good jets
    ###########################################

    # When the miniAOD file is created, the results of several different
    # MET filters are save in a TriggerResults object for the PAT process
    # Look at /PhysicsTools/PatAlgos/python/slimming/metFilterPaths_cff.py
    # for the available filter flags

    # The decision was made to include the filter decision flags
    # as individual branches in the tree

    from AllHadronicSUSY.Utils.filterdecisionproducer_cfi import filterDecisionProducer
    process.METFilters = filterDecisionProducer.clone(
        trigTagArg1  = cms.string('TriggerResults'),
        trigTagArg2  = cms.string(''),
        trigTagArg3  = cms.string(filtertag),
        filterName  =   cms.string("Flag_METFilters"),
        )
    process.Baseline += process.METFilters
    VarsInt.extend(['METFilters'])

    process.CSCTightHaloFilter = filterDecisionProducer.clone(
        trigTagArg1  = cms.string('TriggerResults'),
        trigTagArg2  = cms.string(''),
        trigTagArg3  = cms.string(filtertag),
        filterName  =   cms.string("Flag_CSCTightHaloFilter"),
        )
    process.Baseline += process.CSCTightHaloFilter
    VarsInt.extend(['CSCTightHaloFilter'])

    process.HBHENoiseFilter = filterDecisionProducer.clone(
        trigTagArg1  = cms.string('TriggerResults'),
        trigTagArg2  = cms.string(''),
        trigTagArg3  = cms.string(filtertag),
        filterName  =   cms.string("Flag_HBHENoiseFilter"),
        )
    process.Baseline += process.HBHENoiseFilter
    VarsInt.extend(['HBHENoiseFilter'])

    process.EcalDeadCellTriggerPrimitiveFilter = filterDecisionProducer.clone(
        trigTagArg1  = cms.string('TriggerResults'),
        trigTagArg2  = cms.string(''),
        trigTagArg3  = cms.string(filtertag),
        filterName  =   cms.string("Flag_EcalDeadCellTriggerPrimitiveFilter"),
        )
    process.Baseline += process.EcalDeadCellTriggerPrimitiveFilter
    VarsInt.extend(['EcalDeadCellTriggerPrimitiveFilter'])

    # The trigger results are saved to the tree as a vector
    # Two vectors are saved, one with the names of the triggers
    # the other with the trigger results, the indexing of these two vectors
    # must match

    from AllHadronicSUSY.Utils.triggerproducer_cfi import triggerProducer
    process.TriggerProducer = triggerProducer.clone(
        trigTagArg1  = cms.string('TriggerResults'),
        trigTagArg2  = cms.string(''),
        trigTagArg3  = cms.string('HLT'),
        triggerNameList  =   cms.string(#space-delimited list of trigger names
            'HLT_PFHT350_PFMET100_NoiseCleaned_v1 '\
            'HLT_PFMET170_NoiseCleaned_v1 '\
            'HLT_PFMET170_NoiseCleaned_v2 '\
            'HLT_PFHT350_v1 '\
            'HLT_PFHT800_v1 '\
            'HLT_PFHT900_v1 '\
            'HLT_Ele27_eta2p1_WP85_Gsf_v1 '\
            'HLT_IsoMu20_eta2p1_IterTrk02_v1 '\
            'HLT_PFHT350_PFMET120_NoiseCleaned_v1 '\
            'HLT_Mu15_IsoVVVL_PFHT350_PFMET70_v1 '\
            'HLT_Ele15_IsoVVVL_PFHT350_PFMET70_v1 '\
            'HLT_Mu15_IsoVVVL_PFHT400_PFMET70_v1 '\
            'HLT_Ele15_IsoVVVL_PFHT400_PFMET70_v1 '\
            'HLT_Photon90_CaloIdL_HT500_v2 '\
            'HLT_Photon90_CaloIdL_HT600_v1 '\
            'HLT_DoubleEle8_CaloIdM_Mass8_PFHT300_v2 '\
            'HLT_DoubleMu8_Mass8_PFHT300_v2 '\
            'HLT_Ele27_eta2p1_WPLoose_Gsf_v1 '\
            'HLT_IsoMu17_eta2p1_v2 '
            ),
        )
    process.Baseline += process.TriggerProducer
    VectorInt.extend(['TriggerProducer:PassTrigger'])
    VectorString.extend(['TriggerProducer:TriggerNames'])



    
    ####### Tag And Probe
    from AllHadronicSUSY.Utils.selectpfcandidates_cfi import SelectPFCandidates
    process.SelectedPFCandidatesProbeCands5 = SelectPFCandidates.clone(
    PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
    MinPt								  = cms.double(5),
    MaxEta								  = cms.double(2.5),
    )
    process.SelectedPFCandidatesProbeCands10 = SelectPFCandidates.clone(
    PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
    MinPt								  = cms.double(10),
    MaxEta								  = cms.double(2.5),
    )
    process.SelectedPFElecCandidates = SelectPFCandidates.clone(
    PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
    MinPt								  = cms.double(5),
    MaxEta								  = cms.double(2.5),
    SelectpdgIDTyp							  = cms.int32(11), 
    )
    process.SelectedPFMuCandidates = SelectPFCandidates.clone(
    PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
    MinPt								  = cms.double(5),
    MaxEta								  = cms.double(2.4),
    SelectpdgIDTyp							  = cms.int32(13), 
    )
    process.SelectedPFPionCandidates = SelectPFCandidates.clone(
    PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
    MinPt                                                                 = cms.double(10),
    MaxEta                                                                = cms.double(2.4),
    SelectpdgIDTyp                                                        = cms.int32(211), 
    )
    from AllHadronicSUSY.Utils.activityProducer_cfi import activityProducer
    process.MuonIsoTag = activityProducer.clone(
    objectSource   = cms.InputTag('LeptonsNew:IdMuon'), # probe source
    objectMatchSource   = cms.InputTag('LeptonsNew:IdIsoMuon'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(1),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    TagObjectForMTWComputation = cms.InputTag('LeptonsNew:IdIsoMuon'),
    )
    process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoMuon@+ LeptonsNew:IdMuon@-"), # charge coniugate states are implied
    cut   = cms.string("60.0 < mass < 130.0"),
    )
    process.muonIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairs"),
    #arbitration   = cms.string("OneProbe"),
    arbitration   = cms.string("None"),
    massForArbitration = cms.double(91),
    # variables to use
    variables = cms.PSet(
    ## methods of reco::Candidate
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    #muonsMiniIso = cms.string("muonsMiniIso"),
    #miniIso = cms.string("miniIso"),
    ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
    #nsegm = cms.string("numberOfMatches"), 
    ## this one is an external variable
    #drj = cms.InputTag("drToNearestJet"),
    #nGV = cms.InputTag("goodVertices.size()"),
    #miniIso = cms.InputTag("probeMuons","muonsMiniIso"),
    #miniIso = cms.InputTag("probeMuons","miniIso"),
    activity = cms.InputTag("MuonIsoTag","Activity"),
    Passing = cms.InputTag("MuonIsoTag","Passing"),
    Pt = cms.InputTag("MuonIsoTag","Pt"),
    Eta = cms.InputTag("MuonIsoTag","Eta"),
    MTW = cms.InputTag("MuonIsoTag","MTW"),
    MTWClean = cms.InputTag("MuonIsoTag","MTWClean"),
    RecomputedMET = cms.InputTag("MuonIsoTag","RecomputedMET"),
    TagObjectsNum = cms.InputTag("MuonIsoTag","TagObjectsNum"),
    Weight = cms.InputTag("MuonIsoTag","Weight"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
    ## one defined by an external collection of passing probes
    #passingCal = cms.InputTag("probesPassingCal"), 
    ## two defined by simple string cuts
    #   passingGlb = cms.string("isGlobalMuon"),
    passingIso = cms.InputTag("LeptonsNew:IdMuon"),
    #passingIso2 = cms.InputTag("MuonIsoTag:PassingProbes"),
    #passingGlb = cms.string("Passing<0.5"),
    #passingIso = cms.InputTag("MuonIsoTag","Passing"),
    #passingIso = cms.InputTag("probePassingIso"),
    ),
    # mc-truth info
    isMC = cms.bool(False),
    motherPdgId = cms.vint32(22,23),
    #makeMCUnbiasTree = cms.bool(True),
    #checkMotherInUnbiasEff = cms.bool(True),
    #tagMatches = cms.InputTag("muMcMatch"),
    #probeMatches  = cms.InputTag("muMcMatch"),
    #allProbes     = cms.InputTag("probeMuons"),
    )
    # mu reco
    process.MuonRecoTag = activityProducer.clone(
    #objectSource   = cms.InputTag('SelectedPFCandidatesProbeCands10'), # probe source
    objectSource   = cms.InputTag('SelectedPFMuCandidates'), # probe source
    objectMatchSource   = cms.InputTag('LeptonsNew:IdMuon'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(11),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    TagObjectForMTWComputation = cms.InputTag('LeptonsNew:IdIsoMuon'),
    )
    process.tpPairsMuReco = cms.EDProducer("CandViewShallowCloneCombiner",
    #decay = cms.string("LeptonsNewTag:IdIsoMuon@+ SelectedPFCandidatesProbeCands10@-"), # charge coniugate states are implied
    decay = cms.string("LeptonsNewTag:IdIsoMuon@+ SelectedPFMuCandidates@-"), # charge coniugate states are implied
    cut   = cms.string("60.0 < mass < 130.0"),
    )
    process.muonRecoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsMuReco"),
    #arbitration   = cms.string("OneProbe"),
    arbitration   = cms.string("None"),
    massForArbitration = cms.double(91),
    # variables to use
    variables = cms.PSet(
    ## methods of reco::Candidate
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    #muonsMiniIso = cms.string("muonsMiniIso"),
    #miniIso = cms.string("miniIso"),
    ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
    #nsegm = cms.string("numberOfMatches"), 
    ## this one is an external variable
    #drj = cms.InputTag("drToNearestJet"),
    #nGV = cms.InputTag("goodVertices.size()"),
    #miniIso = cms.InputTag("probeMuons","muonsMiniIso"),
    #miniIso = cms.InputTag("probeMuons","miniIso"),
    activity = cms.InputTag("MuonRecoTag","Activity"),
    Passing = cms.InputTag("MuonRecoTag","Passing"),
    Pt = cms.InputTag("MuonRecoTag","Pt"),
    Eta = cms.InputTag("MuonRecoTag","Eta"),
    MTW = cms.InputTag("MuonRecoTag","MTW"),
    MTWClean = cms.InputTag("MuonRecoTag","MTWClean"),
    RecomputedMET = cms.InputTag("MuonRecoTag","RecomputedMET"),
    TagObjectsNum = cms.InputTag("MuonRecoTag","TagObjectsNum"),
    Weight = cms.InputTag("MuonRecoTag","Weight"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
    ## one defined by an external collection of passing probes
    #passingCal = cms.InputTag("probesPassingCal"), 
    ## two defined by simple string cuts
    #   passingGlb = cms.string("isGlobalMuon"),
    passingIso = cms.InputTag("LeptonsNew:IdMuon"),
    #passingGlb = cms.string("Passing<0.5"),
    #passingIso = cms.InputTag("MuonIsoTag","Passing"),
    #passingIso = cms.InputTag("probePassingIso"),
    ),
    # mc-truth info
    isMC = cms.bool(False),
    motherPdgId = cms.vint32(22,23),
    #makeMCUnbiasTree = cms.bool(True),
    #checkMotherInUnbiasEff = cms.bool(True),
    #tagMatches = cms.InputTag("muMcMatch"),
    #probeMatches  = cms.InputTag("muMcMatch"),
    #allProbes     = cms.InputTag("probeMuons"),
    )
    
    # elec iso
    from AllHadronicSUSY.Utils.activityProducer_cfi import activityProducer
    process.ElectronIsoTag = activityProducer.clone(
    objectSource   = cms.InputTag('LeptonsNew:IdElectron'), # probe source
    objectMatchSource   = cms.InputTag('LeptonsNew:IdIsoElectron'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(2), ## change here for differnt lepton isotrack typ
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    TagObjectForMTWComputation = cms.InputTag('LeptonsNew:IdIsoElectron'),
    )
    process.tpPairsElecIso = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoElectron@+ LeptonsNew:IdElectron@-"), # charge coniugate states are implied
    cut   = cms.string("60.0 < mass < 130.0"),
    )
    process.elecIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsElecIso"),
    #arbitration   = cms.string("OneProbe"),
    arbitration   = cms.string("None"),
    massForArbitration = cms.double(91),
    # variables to use
    variables = cms.PSet(
    ## methods of reco::Candidate
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    #muonsMiniIso = cms.string("muonsMiniIso"),
    #miniIso = cms.string("miniIso"),
    ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
    #nsegm = cms.string("numberOfMatches"), 
    ## this one is an external variable
    #drj = cms.InputTag("drToNearestJet"),
    #nGV = cms.InputTag("goodVertices.size()"),
    #miniIso = cms.InputTag("probeMuons","muonsMiniIso"),
    #miniIso = cms.InputTag("probeMuons","miniIso"),
    activity = cms.InputTag("ElectronIsoTag","Activity"),
    Passing = cms.InputTag("ElectronIsoTag","Passing"),
    Pt = cms.InputTag("ElectronIsoTag","Pt"),
    Eta = cms.InputTag("ElectronIsoTag","Eta"),
    MTW = cms.InputTag("ElectronIsoTag","MTW"),
    MTWClean = cms.InputTag("ElectronIsoTag","MTWClean"),
    RecomputedMET = cms.InputTag("ElectronIsoTag","RecomputedMET"),
    TagObjectsNum = cms.InputTag("ElectronIsoTag","TagObjectsNum"),
    Weight = cms.InputTag("ElectronIsoTag","Weight"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
    ## one defined by an external collection of passing probes
    #passingCal = cms.InputTag("probesPassingCal"), 
    ## two defined by simple string cuts
    #   passingGlb = cms.string("isGlobalMuon"),
    passingIso = cms.InputTag("LeptonsNew:IdMuon"),
    #passingGlb = cms.string("Passing<0.5"),
    #passingIso = cms.InputTag("MuonIsoTag","Passing"),
    #passingIso = cms.InputTag("probePassingIso"),
    ),
    # mc-truth info
    isMC = cms.bool(False),
    motherPdgId = cms.vint32(22,23),
    #makeMCUnbiasTree = cms.bool(True),
    #checkMotherInUnbiasEff = cms.bool(True),
    #tagMatches = cms.InputTag("muMcMatch"),
    #probeMatches  = cms.InputTag("muMcMatch"),
    #allProbes     = cms.InputTag("probeMuons"),
    )
    # elec reco
    process.ElectronRecoTag = activityProducer.clone(
    objectSource   = cms.InputTag('slimmedPhotons'), # probe source
    objectMatchSource   = cms.InputTag('LeptonsNew:IdElectron'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(22),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    TagObjectForMTWComputation = cms.InputTag('LeptonsNew:IdIsoElectron'),
    )
    process.tpPairsElecReco = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoElectron@+ slimmedPhotons"), # charge coniugate states are implied
    cut   = cms.string("60.0 < mass < 130.0"),
    )
    process.elecRecoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsElecReco"),
    #arbitration   = cms.string("OneProbe"),
    arbitration   = cms.string("None"),
    massForArbitration = cms.double(91),
    # variables to use
    variables = cms.PSet(
    ## methods of reco::Candidate
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    #muonsMiniIso = cms.string("muonsMiniIso"),
    #miniIso = cms.string("miniIso"),
    ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
    #nsegm = cms.string("numberOfMatches"), 
    ## this one is an external variable
    #drj = cms.InputTag("drToNearestJet"),
    #nGV = cms.InputTag("goodVertices.size()"),
    #miniIso = cms.InputTag("probeMuons","muonsMiniIso"),
    #miniIso = cms.InputTag("probeMuons","miniIso"),
    activity = cms.InputTag("ElectronRecoTag","Activity"),
    Passing = cms.InputTag("ElectronRecoTag","Passing"),
    Pt = cms.InputTag("ElectronRecoTag","Pt"),
    Eta = cms.InputTag("ElectronRecoTag","Eta"),
    MTW = cms.InputTag("ElectronRecoTag","MTW"),
    MTWClean = cms.InputTag("ElectronRecoTag","MTWClean"),
    RecomputedMET = cms.InputTag("ElectronRecoTag","RecomputedMET"),
    TagObjectsNum = cms.InputTag("ElectronRecoTag","TagObjectsNum"),
    Weight = cms.InputTag("ElectronRecoTag","Weight"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
    ## one defined by an external collection of passing probes
    #passingCal = cms.InputTag("probesPassingCal"), 
    ## two defined by simple string cuts
    #   passingGlb = cms.string("isGlobalMuon"),
    passingIso = cms.InputTag("LeptonsNew:IdMuon"),
    #passingGlb = cms.string("Passing<0.5"),
    #passingIso = cms.InputTag("MuonIsoTag","Passing"),
    #passingIso = cms.InputTag("probePassingIso"),
    ),
    # mc-truth info
    isMC = cms.bool(False),
    motherPdgId = cms.vint32(22,23),
    #makeMCUnbiasTree = cms.bool(True),
    #checkMotherInUnbiasEff = cms.bool(True),
    #tagMatches = cms.InputTag("muMcMatch"),
    #probeMatches  = cms.InputTag("muMcMatch"),
    #allProbes     = cms.InputTag("probeMuons"),
    )
    # isolated track muons
    process.IsoTrackMuonTag = activityProducer.clone(
    #objectSource   = cms.InputTag('SelectedPFCandidatesProbeCands5'), # probe source
    objectSource   = cms.InputTag('SelectedPFMuCandidates'), # probe source
    objectMatchSource   = cms.InputTag('IsolatedMuonTracksVeto'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(3),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    TagObjectForMTWComputation = cms.InputTag('LeptonsNewTag:IdIsoMuon'),
    METTag = cms.InputTag('slimmedMETs'), 
    )
    process.tpPairsIsoTrackMu = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoMuon@+ SelectedPFMuCandidates@-"), # charge coniugate states are implied
    #decay = cms.string("LeptonsNewTag:IdIsoMuon@+ SelectedPFCandidatesProbeCands5@-"), # charge coniugate states are implied
    cut   = cms.string("60.0 < mass < 130.0"),
    )
    process.IsoTrackMuonIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsIsoTrackMu"),
    #arbitration   = cms.string("OneProbe"),
    arbitration   = cms.string("None"),
    massForArbitration = cms.double(91),
    # variables to use
    variables = cms.PSet(
    ## methods of reco::Candidate
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    #muonsMiniIso = cms.string("muonsMiniIso"),
    #miniIso = cms.string("miniIso"),
    ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
    #nsegm = cms.string("numberOfMatches"), 
    ## this one is an external variable
    #drj = cms.InputTag("drToNearestJet"),
    #nGV = cms.InputTag("goodVertices.size()"),
    #miniIso = cms.InputTag("probeMuons","muonsMiniIso"),
    #miniIso = cms.InputTag("probeMuons","miniIso"),
    activity = cms.InputTag("IsoTrackMuonTag","Activity"),
    Passing = cms.InputTag("IsoTrackMuonTag","Passing"),
    Pt = cms.InputTag("IsoTrackMuonTag","Pt"),
    Eta = cms.InputTag("IsoTrackMuonTag","Eta"),
    MTW = cms.InputTag("IsoTrackMuonTag","MTW"),
    MTWClean = cms.InputTag("IsoTrackMuonTag","MTWClean"),
    RecomputedMET = cms.InputTag("IsoTrackMuonTag","RecomputedMET"),
    TagObjectsNum = cms.InputTag("IsoTrackMuonTag","TagObjectsNum"),
    Weight = cms.InputTag("IsoTrackMuonTag","Weight"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
    ## one defined by an external collection of passing probes
    #passingCal = cms.InputTag("probesPassingCal"), 
    ## two defined by simple string cuts
    #   passingGlb = cms.string("isGlobalMuon"),
    passingIso = cms.InputTag("LeptonsNew:IdMuon"),
    #passingIso2 = cms.InputTag("MuonIsoTag:PassingProbes"),
    #passingGlb = cms.string("Passing<0.5"),
    #passingIso = cms.InputTag("MuonIsoTag","Passing"),
    #passingIso = cms.InputTag("probePassingIso"),
    ),
    # mc-truth info
    isMC = cms.bool(False),
    motherPdgId = cms.vint32(22,23),
    #makeMCUnbiasTree = cms.bool(True),
    #checkMotherInUnbiasEff = cms.bool(True),
    #tagMatches = cms.InputTag("muMcMatch"),
    #probeMatches  = cms.InputTag("muMcMatch"),
    #allProbes     = cms.InputTag("probeMuons"),
    )
    # isolated track electrons
    process.IsoTrackElecTag = activityProducer.clone(
    objectSource   = cms.InputTag('SelectedPFElecCandidates'), # probe source
    #objectSource   = cms.InputTag('SelectedPFCandidatesProbeCands5'), # probe source
    objectMatchSource   = cms.InputTag('IsolatedElectronTracksVeto'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(4),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    TagObjectForMTWComputation = cms.InputTag('LeptonsNewTag:IdIsoElectron'),
    METTag = cms.InputTag('slimmedMETs'), 
    )
    process.tpPairsIsoTrackElec = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoElectron@+ SelectedPFElecCandidates@-"), # charge coniugate states are implied
    #decay = cms.string("LeptonsNewTag:IdIsoElectron@+ SelectedPFCandidatesProbeCands5@-"), # charge coniugate states are implied
    cut   = cms.string("60.0 < mass < 130.0"),
    )
    process.IsoTrackElecIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsIsoTrackElec"),
    #arbitration   = cms.string("OneProbe"),
    arbitration   = cms.string("None"),
    massForArbitration = cms.double(91),
    # variables to use
    variables = cms.PSet(
    ## methods of reco::Candidate
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    #muonsMiniIso = cms.string("muonsMiniIso"),
    #miniIso = cms.string("miniIso"),
    ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
    #nsegm = cms.string("numberOfMatches"), 
    ## this one is an external variable
    #drj = cms.InputTag("drToNearestJet"),
    #nGV = cms.InputTag("goodVertices.size()"),
    #miniIso = cms.InputTag("probeMuons","muonsMiniIso"),
    #miniIso = cms.InputTag("probeMuons","miniIso"),
    activity = cms.InputTag("IsoTrackElecTag","Activity"),
    Passing = cms.InputTag("IsoTrackElecTag","Passing"),
    Pt = cms.InputTag("IsoTrackElecTag","Pt"),
    Eta = cms.InputTag("IsoTrackElecTag","Eta"),
    MTW = cms.InputTag("IsoTrackElecTag","MTW"),
    MTWClean = cms.InputTag("IsoTrackElecTag","MTWClean"),
    RecomputedMET = cms.InputTag("IsoTrackElecTag","RecomputedMET"),
    TagObjectsNum = cms.InputTag("IsoTrackElecTag","TagObjectsNum"),
    Weight = cms.InputTag("IsoTrackElecTag","Weight"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
    ## one defined by an external collection of passing probes
    #passingCal = cms.InputTag("probesPassingCal"), 
    ## two defined by simple string cuts
    #   passingGlb = cms.string("isGlobalMuon"),
    passingIso = cms.InputTag("LeptonsNew:IdMuon"),
    #passingIso2 = cms.InputTag("MuonIsoTag:PassingProbes"),
    #passingGlb = cms.string("Passing<0.5"),
    #passingIso = cms.InputTag("MuonIsoTag","Passing"),
    #passingIso = cms.InputTag("probePassingIso"),
    ),
    # mc-truth info
    isMC = cms.bool(False),
    motherPdgId = cms.vint32(22,23),
    #makeMCUnbiasTree = cms.bool(True),
    #checkMotherInUnbiasEff = cms.bool(True),
    #tagMatches = cms.InputTag("muMcMatch"),
    #probeMatches  = cms.InputTag("muMcMatch"),
    #allProbes     = cms.InputTag("probeMuons"),
    )
    # isolated track pion
    process.IsoTrackPionTag = activityProducer.clone(
    objectSource   = cms.InputTag('SelectedPFPionCandidates'), # probe source
    #objectSource   = cms.InputTag('SelectedPFCandidatesProbeCands5'), # probe source
    objectMatchSource   = cms.InputTag('IsolatedPionTracksVeto'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(5),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    TagObjectForMTWComputation = cms.InputTag('IsolatedPionTracksVeto'),
    METTag = cms.InputTag('slimmedMETs'), 
    )
    process.tpPairsIsoTrackPion = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("IsolatedPionTracksVeto@+ SelectedPFPionCandidates@-"), # charge coniugate states are implied
    #decay = cms.string("LeptonsNewTag:IdIsoElectron@+ SelectedPFCandidatesProbeCands5@-"), # charge coniugate states are implied
    cut   = cms.string("60.0 < mass < 130.0"),
    )
    process.IsoTrackPionIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsIsoTrackPion"),
    #arbitration   = cms.string("OneProbe"),
    arbitration   = cms.string("None"),
    massForArbitration = cms.double(91),
    # variables to use
    variables = cms.PSet(
    ## methods of reco::Candidate
    eta = cms.string("eta"),
    pt  = cms.string("pt"),
    #muonsMiniIso = cms.string("muonsMiniIso"),
    #miniIso = cms.string("miniIso"),
    ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
    #nsegm = cms.string("numberOfMatches"), 
    ## this one is an external variable
    #drj = cms.InputTag("drToNearestJet"),
    #nGV = cms.InputTag("goodVertices.size()"),
    #miniIso = cms.InputTag("probeMuons","muonsMiniIso"),
    #miniIso = cms.InputTag("probeMuons","miniIso"),
    activity = cms.InputTag("IsoTrackPionTag","Activity"),
    Passing = cms.InputTag("IsoTrackPionTag","Passing"),
    Pt = cms.InputTag("IsoTrackPionTag","Pt"),
    Eta = cms.InputTag("IsoTrackPionTag","Eta"),
    MTW = cms.InputTag("IsoTrackPionTag","MTW"),
    RecomputedMET = cms.InputTag("IsoTrackPionTag","RecomputedMET"),
    TagObjectsNum = cms.InputTag("IsoTrackPionTag","TagObjectsNum"),
     Weight = cms.InputTag("IsoTrackPionTag","Weight"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
    ## one defined by an external collection of passing probes
    #passingCal = cms.InputTag("probesPassingCal"), 
    ## two defined by simple string cuts
    #   passingGlb = cms.string("isGlobalMuon"),
    passingIso = cms.InputTag("LeptonsNew:IdMuon"),
    #passingIso2 = cms.InputTag("MuonIsoTag:PassingProbes"),
    #passingGlb = cms.string("Passing<0.5"),
    #passingIso = cms.InputTag("MuonIsoTag","Passing"),
    #passingIso = cms.InputTag("probePassingIso"),
    ),
    # mc-truth info
    isMC = cms.bool(False),
    motherPdgId = cms.vint32(22,23),
    #makeMCUnbiasTree = cms.bool(True),
    #checkMotherInUnbiasEff = cms.bool(True),
    #tagMatches = cms.InputTag("muMcMatch"),
    #probeMatches  = cms.InputTag("muMcMatch"),
    #allProbes     = cms.InputTag("probeMuons"),
    )
    from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
    process.HTJets = SubJetSelection.clone(
    JetTag  = cms.InputTag('GoodJets'),
    MinPt								  = cms.double(30),
    MaxEta								  = cms.double(2.4),
    )
    process.Baseline += process.HTJets
    from AllHadronicSUSY.Utils.htdouble_cfi import htdouble
    process.HT = htdouble.clone(
    JetTag  = cms.InputTag('HTJets'),
    )
    process.Baseline += process.HT
    VarsDouble.extend(['HT'])
    from AllHadronicSUSY.Utils.doublefilter_cfi import DoubleFilter
    process.HTFilter = DoubleFilter.clone(
    DoubleTag          = cms.InputTag('HT'),
    CutValue	= cms.double('500'),
    )
    from AllHadronicSUSY.Utils.njetint_cfi import njetint
    process.NJets = njetint.clone(
    JetTag  = cms.InputTag('HTJets'),
    )
    process.Baseline += process.NJets
    VarsInt.extend(['NJets'])
    from AllHadronicSUSY.Utils.btagint_cfi import btagint
    process.BTags = btagint.clone(
    JetTag  = cms.InputTag('HTJets'),
    BTagInputTag	        = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
    BTagCutValue					= cms.double(0.814)
    )
    process.Baseline += process.BTags
    VarsInt.extend(['BTags'])
    from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
    process.MHTJets = SubJetSelection.clone(
    JetTag  = cms.InputTag('GoodJets'),
    MinPt								  = cms.double(30),
    MaxEta								  = cms.double(5.0),
    )
    process.Baseline += process.MHTJets
    from AllHadronicSUSY.Utils.mhtdouble_cfi import mhtdouble
    process.MHT = mhtdouble.clone(
    JetTag  = cms.InputTag('MHTJets'),
    )
    process.Baseline += process.MHT
    VarsDouble.extend(['MHT:Pt(MHT)','MHT:Phi(MHT_Phi)'])
    process.MHTFilter = DoubleFilter.clone(
    DoubleTag          = cms.InputTag('MHT:Pt'),
    CutValue	= cms.double('200'),
    )
    if applybaseline:
			process.Baseline += process.HTFilter
			#process.Baseline += process.MHTFilter
    from AllHadronicSUSY.Utils.deltaphidouble_cfi import deltaphidouble
    process.DeltaPhi = deltaphidouble.clone(
    DeltaPhiJets  = cms.InputTag('HTJets'),
    MHTJets  = cms.InputTag("MHTJets"),
    )
    process.Baseline += process.DeltaPhi
    VarsDouble.extend(['DeltaPhi:DeltaPhi1','DeltaPhi:DeltaPhi2','DeltaPhi:DeltaPhi3'])
    from AllHadronicSUSY.Utils.metdouble_cfi import metdouble
    process.MET = metdouble.clone(
    METTag  = cms.InputTag("slimmedMETs"),
    JetTag  = cms.InputTag('HTJets'),
    )
    process.Baseline += process.MET
    VarsDouble.extend(['MET:minDeltaPhiN','MET:DeltaPhiN1','MET:DeltaPhiN2','MET:DeltaPhiN3','MET:Pt(METPt)','MET:Phi(METPhi)'])
    #lost-lepton producers
    from AllHadronicSUSY.Utils.jetproperties_cfi import jetproperties
    process.JetsProperties = jetproperties.clone(
    JetTag  = cms.InputTag('HTJets'),
    BTagInputTag	        = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
    METTag  = cms.InputTag("slimmedMETs"),
    )
    process.Baseline += process.JetsProperties
    if geninfo : 
        from AllHadronicSUSY.Utils.genLeptonRecoCand_cfi import genLeptonRecoCand
        process.GenLeptons = genLeptonRecoCand.clone(
            PrunedGenParticleTag  = cms.InputTag("prunedGenParticles"),
            )
        process.LostLepton += process.GenLeptons

    process.SelectedPFCandidates = SelectPFCandidates.clone(
    PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
    MinPt								  = cms.double(4),
    MaxEta								  = cms.double(5.0),
    )
    process.LostLepton += process.SelectedPFCandidates

    #define sequences
    
    #baseline RA2/b variables default shared variables
    if geninfo :
        RecoCandVector.extend(['LeptonsNew:IdIsoMuon(Muons)','LeptonsNew:IdIsoElectron(Electrons)'])

    ## --- Final paths ----------------------------------------------------

    # put together final sequence with optional producers
    process.AdditionalSequence = cms.Sequence()
    if lostlepton:
      print "Adding LostLepton calculations to final path and tree"
      process.AdditionalSequence += process.LostLepton 
      process.AdditionalSequence += process.SelectedPFElecCandidates
      process.AdditionalSequence += process.SelectedPFMuCandidates
      process.AdditionalSequence += process.SelectedPFPionCandidates
    #  VarsRecoCand = cms.vstring('selectedIDIsoMuons','selectedIDMuons','selectedIDIsoElectrons','selectedIDMuons','IsolatedTracks','HTJets'),
   #   RecoCandVector.extend(['selectedIDIsoMuons','selectedIDMuons','selectedIDIsoElectrons','selectedIDElectrons','IsolatedTracks']),
      RecoCandVector.extend(['IsolatedElectronTracksVeto|IsolatedElectronTracksVeto:MT(F_MT)','IsolatedMuonTracksVeto|IsolatedMuonTracksVeto:MT(F_MT)','IsolatedPionTracksVeto|IsolatedPionTracksVeto:MT(F_MT)','LeptonsNew:IdIsoMuon(selectedIDIsoMuons)|LeptonsNew:MuIDIsoMTW(F_MTW)','LeptonsNew:IdMuon(selectedIDMuons)|LeptonsNew:MuIDMTW(F_MTW)','LeptonsNew:IdIsoElectron(selectedIDIsoElectrons)|LeptonsNew:ElecIDIsoMTW(F_MTW)','LeptonsNew:IdElectron(selectedIDElectrons)|LeptonsNew:ElecIDMTW(F_MTW)','SelectedPFCandidates|SelectedPFCandidates:Charge(I_Charge)|SelectedPFCandidates:Typ(I_Typ)']),
      if geninfo :
          RecoCandVector.extend(['GenLeptons:Boson(GenBoson)|GenLeptons:BosonPDGId(I_GenBosonPDGId)','GenLeptons:Muon(GenMu)|GenLeptons:MuonTauDecay(I_GenMuFromTau)' ,'GenLeptons:Electron(GenElec)|GenLeptons:ElectronTauDecay(I_GenElecFromTau)','GenLeptons:Tau(GenTau)|GenLeptons:TauHadronic(I_GenTauHad)'] ) # gen information on leptons
          RecoCandVector.extend(['GenLeptons:TauDecayCands(TauDecayCands)|GenLeptons:TauDecayCandspdgID(I_pdgID)'])
      RecoCandVector.extend(['LeptonsNewTag:IdIsoMuon(selectedIDIsoMuonsNoMiniIso)','LeptonsNewTag:IdIsoElectron(selectedIDIsoElectronsNoMiniIso)'] ) # gen information on leptons
      RecoCandVector.extend(['JetsProperties(Jets)|JetsProperties:bDiscriminatorUser(F_bDiscriminator)|JetsProperties:chargedEmEnergyFraction(F_chargedEmEnergyFraction)|JetsProperties:chargedHadronEnergyFraction(F_chargedHadronEnergyFraction)|JetsProperties:chargedHadronMultiplicity(I_chargedHadronMultiplicity)|JetsProperties:electronMultiplicity(I_electronMultiplicity)|JetsProperties:jetArea(F_jetArea)|JetsProperties:muonEnergyFraction(F_muonEnergyFraction)|JetsProperties:muonMultiplicity(I_muonMultiplicity)|JetsProperties:neutralEmEnergyFraction(F_neutralEmEnergyFraction)|JetsProperties:neutralHadronMultiplicity(I_neutralHadronMultiplicity)|JetsProperties:photonEnergyFraction(F_photonEnergyFraction)|JetsProperties:photonMultiplicity(I)'] ) # jet information on various variables
      RecoCandVector.extend(['slimmedElectrons','slimmedMuons'])
      RecoCandVector.extend(['SelectedPFElecCandidates','SelectedPFMuCandidates','SelectedPFPionCandidates'])

    process.dump = cms.EDAnalyzer("EventContentAnalyzer")
    #tag and probe
    if tagandprobe:
        process.Baseline += process.SelectedPFCandidatesProbeCands5
        process.Baseline += process.SelectedPFCandidatesProbeCands10
        process.Baseline += process.SelectedPFElecCandidates
        process.Baseline += process.SelectedPFMuCandidates
        process.Baseline += process.SelectedPFPionCandidates
        if geninfo : 
            process.Baseline += process.GenLeptons
        process.Baseline += process.JetsProperties
        process.Baseline += process.SelectedPFCandidates
        process.Baseline += process.MuonIsoTag
        process.Baseline += process.tpPairs
        process.Baseline += process.muonIsoEffs
        process.Baseline += process.MuonRecoTag
        process.Baseline += process.tpPairsMuReco
        process.Baseline += process.muonRecoEffs
        process.Baseline += process.ElectronIsoTag
        process.Baseline += process.tpPairsElecIso
        process.Baseline += process.elecIsoEffs
        process.Baseline += process.ElectronRecoTag
        process.Baseline += process.tpPairsElecReco
        process.Baseline += process.elecRecoEffs
        process.Baseline += process.IsoTrackMuonTag
        process.Baseline += process.tpPairsIsoTrackMu
        process.Baseline += process.IsoTrackMuonIsoEffs
        process.Baseline += process.IsoTrackElecTag
        process.Baseline += process.tpPairsIsoTrackElec
        process.Baseline += process.IsoTrackElecIsoEffs
        process.Baseline += process.IsoTrackPionTag
        process.Baseline += process.tpPairsIsoTrackPion
        process.Baseline += process.IsoTrackPionIsoEffs
        RecoCandVector.extend(['slimmedPhotons'])

	### begin Zinv stuff ###
    if doZinv:   
        ##### add branches for photon studies
        process.TreeMaker2.VectorDouble.append("goodPhotons:isEB(photon_isEB)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:genMatched(photon_genMatched)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:hadTowOverEM(photon_hadTowOverEM)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:hasPixelSeed(photon_hasPixelSeed)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:passElectronVeto(photon_passElectronVeto)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIso(photon_pfChargedIso)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:pfChargedIsoRhoCorr(photon_pfChargedIsoRhoCorr)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIso(photon_pfGammaIso)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:pfGammaIsoRhoCorr(photon_pfGammaIsoRhoCorr)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIso(photon_pfNeutralIso)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:pfNeutralIsoRhoCorr(photon_pfNeutralIsoRhoCorr)")
        process.TreeMaker2.VectorDouble.append("goodPhotons:sigmaIetaIeta(photon_sigmaIetaIeta)")

        process.slimmedPhotons4Vec = cms.EDProducer("fourVectorProducer",
                                                    particleCollection = cms.untracked.InputTag("slimmedPhotons"),
                                                    debug = cms.untracked.bool(False)
                                                    )
        
        process.TreeMaker2.VectorTLorentzVector.append("slimmedPhotons4Vec(photonCands)")
        
        process.ZinvClean = cms.Sequence()

        from AllHadronicSUSY.Utils.zproducer_cfi import ZProducer
        process.maketheZs = ZProducer.clone(
        ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
        MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon')
        )
        process.ZinvClean += process.maketheZs
        VarsInt.extend(['maketheZs:ZNum'])
        VectorTLorentzVector.append("maketheZs:Zp4")
        
        from AllHadronicSUSY.Utils.jetcleaner_cfi import JetCleaner
        process.cleanTheJets = JetCleaner.clone(
           JetTag  = cms.InputTag('GoodJets'),
           ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
           ElectronR = cms.double(0.4),
           MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon'),
           MuonR = cms.double(0.4),
           PhotonTag = cms.InputTag('goodPhotons', 'bestPhoton'),
           PhotonR = cms.double(0.4)
        )
        process.ZinvClean += process.cleanTheJets

        from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
        process.HTJetsclean = SubJetSelection.clone(
           JetTag = cms.InputTag('cleanTheJets', 'GoodJetsclean'),
           MinPt = cms.double(30),
           MaxEta = cms.double(2.4),
        )
        process.ZinvClean += process.HTJetsclean

        from AllHadronicSUSY.Utils.htdouble_cfi import htdouble
        process.HTclean = htdouble.clone(
           JetTag = cms.InputTag('HTJetsclean'),
        )
        process.ZinvClean += process.HTclean
        VarsDouble.extend(['HTclean'])

        from AllHadronicSUSY.Utils.njetint_cfi import njetint
        process.NJetsclean = njetint.clone(
           JetTag = cms.InputTag('HTJetsclean'),
        )
        process.ZinvClean += process.NJetsclean
        VarsInt.extend(['NJetsclean'])

        from AllHadronicSUSY.Utils.btagint_cfi import btagint
        process.BTagsclean = btagint.clone(
           JetTag = cms.InputTag('HTJetsclean'),
           BTagInputTag = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
           BTagCutValue = cms.double(0.814)
        )
        process.ZinvClean += process.BTagsclean
        VarsInt.extend(['BTagsclean'])

        from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
        process.MHTJetsclean = SubJetSelection.clone(
           JetTag = cms.InputTag('cleanTheJets', 'GoodJetsclean'),
           MinPt = cms.double(30),
           MaxEta = cms.double(5.0),
        )
        process.ZinvClean += process.MHTJetsclean

        process.DeltaPhiClean = deltaphidouble.clone(
            DeltaPhiJets  = cms.InputTag('HTJetsclean'),
            MHTJets  = cms.InputTag("MHTJetsclean"),
            )
        process.ZinvClean += process.DeltaPhiClean
        VarsDouble.extend(['DeltaPhiClean:DeltaPhi1(DeltaPhi1clean)','DeltaPhiClean:DeltaPhi2(DeltaPhi2clean)','DeltaPhiClean:DeltaPhi3(DeltaPhi3clean)',])
        
        from AllHadronicSUSY.Utils.subJetSelection_cfi import SubJetSelection
        from AllHadronicSUSY.Utils.mhtdouble_cfi import mhtdouble
        process.MHTclean = mhtdouble.clone(
           JetTag = cms.InputTag('MHTJetsclean'),
        )
        process.ZinvClean += process.MHTclean
        VarsDouble.extend(['MHTclean:Pt(MHTclean)'])

        from AllHadronicSUSY.Utils.metdouble_cfi import metdouble
        process.METclean = metdouble.clone(
           METTag = cms.InputTag("slimmedMETs"),
           JetTag = cms.InputTag('HTJetsclean'),
           cleanTag = cms.untracked.VInputTag(cms.InputTag('LeptonsNew:IdIsoElectron'), cms.InputTag('LeptonsNew:IdIsoMuon'), cms.InputTag('goodPhotons', 'bestPhoton'))
        )
        process.ZinvClean += process.METclean
        VarsDouble.extend(['METclean:minDeltaPhiN(minDeltaPhiNclean)', 'METclean:Pt(METPtclean)'])

        process.AdditionalSequence += process.ZinvClean
        process.AdditionalSequence += process.slimmedPhotons4Vec 

    ### end Zinv stuff ###

    process.WriteTree = cms.Path(
        process.Baseline *
        process.AdditionalSequence *
#        process.dump *
        process.TreeMaker2
    )

