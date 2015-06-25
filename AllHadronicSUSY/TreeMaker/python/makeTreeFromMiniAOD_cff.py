# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms

def makeTreeFromMiniAOD(
process,
outFileName,
reportEveryEvt=10,
testFileName="",
Global_Tag="",
numProcessedEvt=-1,
lostlepton=False,
gammajets=False,
tagandprobe=False,
applybaseline=False,
doZinv=False
):

    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
    process.GlobalTag.globaltag = Global_Tag

    ## --- Log output ------------------------------------------------------
    process.load("FWCore.MessageService.MessageLogger_cfi")
    process.MessageLogger.cerr = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
        )
    process.MessageLogger.cout = cms.untracked.PSet(
        INFO = cms.untracked.PSet(reportEvery = cms.untracked.int32(reportEveryEvt))
        )
    process.options = cms.untracked.PSet(
        wantSummary = cms.untracked.bool(True)
        ) 


    ## --- Files to process ------------------------------------------------
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(numProcessedEvt)
        )
    process.source = cms.Source("PoolSource",

        fileNames = cms.untracked.vstring(testFileName)
 #       fileNames = cms.untracked.vstring(
 #		'file:/nfs/dust/cms/user/csander/LHE/workdir/simulation_test/T1qqqqHV/output_66.root'
#		)
        )
        
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
    VectorString = cms.vstring()
    VectorInt = cms.vstring()
    # baseline producers
    process.Baseline = cms.Sequence(
    )
    #special sequences
    #lost-lepton variables
    process.LostLepton = cms.Sequence(
      
    )
    #gamma+jet variables
    process.GammaJet = cms.Sequence(
      
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

    from AllHadronicSUSY.Utils.primaryverticesint_cfi import primaryverticesint
    process.NVtx = primaryverticesint.clone(
      VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices')
    )
    process.Baseline += process.NVtx
    VarsInt.extend(['NVtx'])

    ## isotrack producer
    from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationFilter
    from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationCounter
    
    process.IsolatedElectronTracksVeto = trackIsolationFilter.clone(
      doTrkIsoVeto= False,
      vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
      pfCandidatesTag = cms.InputTag("packedPFCandidates"),
      dR_ConeSize         = cms.double(0.3),
      dz_CutValue         = cms.double(0.05),
      minPt_PFCandidate   = cms.double(5.0),
      isoCut              = cms.double(0.2),
      pdgId               = cms.int32(11),
      mTCut=cms.double(100.),
      )

    process.IsolatedMuonTracksVeto = trackIsolationFilter.clone(
      doTrkIsoVeto= False,
      vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
      pfCandidatesTag = cms.InputTag("packedPFCandidates"),
      dR_ConeSize         = cms.double(0.3),
      dz_CutValue         = cms.double(0.05),
      minPt_PFCandidate   = cms.double(5.0),
      isoCut              = cms.double(0.2), 
      pdgId               = cms.int32(13),
      mTCut=cms.double(100.),
      )

    process.IsolatedPionTracksVeto = trackIsolationFilter.clone(
      doTrkIsoVeto= False,
      vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
      pfCandidatesTag = cms.InputTag("packedPFCandidates"),
      dR_ConeSize         = cms.double(0.3),
      dz_CutValue         = cms.double(0.05),
      minPt_PFCandidate   = cms.double(10.0),
      isoCut              = cms.double(0.1),
      pdgId               = cms.int32(211),
      mTCut=cms.double(100.),
      )

    process.Baseline += process.IsolatedElectronTracksVeto
    process.Baseline += process.IsolatedMuonTracksVeto
    process.Baseline += process.IsolatedPionTracksVeto

    VarsInt.extend(['IsolatedElectronTracksVeto:isoTracks(isoElectronTracks)'])
    VarsInt.extend(['IsolatedMuonTracksVeto:isoTracks(isoMuonTracks)'])
    VarsInt.extend(['IsolatedPionTracksVeto:isoTracks(isoPionTracks)'])

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
      )
    process.Baseline += process.LeptonsNewTag
    VarsInt.extend(['LeptonsNewTag(TagLeptonHighPT)'])

    ####### good photons
    process.goodPhotons = cms.EDProducer("PhotonIDisoProducer",
                                         photonCollection = cms.untracked.InputTag("slimmedPhotons"),
                                         rhoCollection = cms.untracked.InputTag("fixedGridRhoFastjetAll"), 
                                         debug = cms.untracked.bool(False)
                                         )
    process.Baseline += process.goodPhotons
    ######  done with photons -- good photon tag is InputTag('goodPhotons','bestPhoton')
    #################################

    ####### good jets -- the start of everything    

    ####### JECs
    # get the JECs
    # this requires the user to download the .db file from this twiki
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC
    ######
    from CondCore.DBCommon.CondDBSetup_cfi import *
    process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
                               connect = cms.string('sqlite_file:PHYS14_V4_MC.db'),
                               toGet = cms.VPSet(
            cms.PSet(record = cms.string("JetCorrectionsRecord"),
                     tag = cms.string("JetCorrectorParametersCollection_PHYS14_V4_MC_AK4PFchs"),
                     label= cms.untracked.string("AK4PFchs")
                     )
            )
                               )
    process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")
    
    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetCorrFactorsUpdated
    process.patJetCorrFactorsReapplyJEC = patJetCorrFactorsUpdated.clone(
        src = cms.InputTag("slimmedJets"),
        levels = ['L1FastJet', 
                  'L2Relative', 
                  'L3Absolute'],
        payload = 'AK4PFchs' ) # Make sure to choose the appropriate levels and payload here!
    
    from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import patJetsUpdated
    process.patJetsReapplyJEC = patJetsUpdated.clone(
        jetSource = cms.InputTag("slimmedJets"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
        )
    ########
    process.Baseline += process.patJetCorrFactorsReapplyJEC
    process.Baseline += process.patJetsReapplyJEC

    ############
    from AllHadronicSUSY.Utils.goodjetsproducer_cfi import GoodJetsProducer
    process.GoodJets = GoodJetsProducer.clone(
      TagMode = cms.bool(True),
      JetTag= cms.InputTag('slimmedJets'),
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
            'HLT_DoubelMu8_Mass8_PFHT300_v2 '
            ),
        )
    process.Baseline += process.TriggerProducer
    VectorInt.extend(['TriggerProducer:PassTrigger'])
    VectorString.extend(['TriggerProducer:TriggerNames'])
    

    
    ####### Tag And Probe
    from AllHadronicSUSY.Utils.activityProducer_cfi import activityProducer
    process.MuonIsoTag = activityProducer.clone(
    objectSource   = cms.InputTag('LeptonsNew:IdMuon'), # probe source
    objectMatchSource   = cms.InputTag('LeptonsNew:IdIsoMuon'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(1),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    )
    process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoMuon@+ LeptonsNew:IdMuon@-"), # charge coniugate states are implied
    cut   = cms.string("70.0 < mass < 130.0"),
    )
    process.muonIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairs"),
    arbitration   = cms.string("OneProbe"),
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
    objectSource   = cms.InputTag('packedPFCandidates'), # probe source
    objectMatchSource   = cms.InputTag('LeptonsNew:IdMuon'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(11),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    )
    process.tpPairsMuReco = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoMuon@+ packedPFCandidates@-"), # charge coniugate states are implied
    cut   = cms.string("70.0 < mass < 130.0"),
    )
    process.muonRecoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsMuReco"),
    arbitration   = cms.string("OneProbe"),
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
    )
    process.tpPairsElecIso = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoElectron@+ LeptonsNew:IdElectron@-"), # charge coniugate states are implied
    cut   = cms.string("70.0 < mass < 130.0"),
    )
    process.elecIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsElecIso"),
    arbitration   = cms.string("OneProbe"),
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
    )
    process.tpPairsElecReco = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoElectron@+ slimmedPhotons"), # charge coniugate states are implied
    cut   = cms.string("70.0 < mass < 130.0"),
    )
    process.elecRecoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsElecReco"),
    arbitration   = cms.string("OneProbe"),
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
    objectSource   = cms.InputTag('packedPFCandidates'), # probe source
    objectMatchSource   = cms.InputTag('IsolatedMuonTracksVeto'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(3),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    )
    process.tpPairsIsoTrackMu = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoMuon@+ packedPFCandidates@-"), # charge coniugate states are implied
    cut   = cms.string("70.0 < mass < 130.0"),
    )
    process.IsoTrackMuonIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsIsoTrackMu"),
    arbitration   = cms.string("OneProbe"),
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
    objectSource   = cms.InputTag('packedPFCandidates'), # probe source
    objectMatchSource   = cms.InputTag('IsolatedElectronTracksVeto'), # to be matched to collection  (IDIsoMuons)
    objectTyp = cms.int32(4),
    activityTyp = cms.int32(0),
    maxDeltaR = cms.double(1.0),
    jetSrc = cms.InputTag('HTJets'),
    )
    process.tpPairsIsoTrackElec = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("LeptonsNewTag:IdIsoElectron@+ packedPFCandidates@-"), # charge coniugate states are implied
    cut   = cms.string("70.0 < mass < 130.0"),
    )
    process.IsoTrackElecIsoEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    tagProbePairs = cms.InputTag("tpPairsIsoTrackElec"),
    arbitration   = cms.string("OneProbe"),
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
    VarsDouble.extend(['MHT'])
    process.MHTFilter = DoubleFilter.clone(
    DoubleTag          = cms.InputTag('MHT'),
    CutValue	= cms.double('200'),
    )
    if applybaseline:
			process.Baseline += process.HTFilter
			process.Baseline += process.MHTFilter
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
    from AllHadronicSUSY.Utils.genLeptonRecoCand_cfi import genLeptonRecoCand
    process.GenLeptons = genLeptonRecoCand.clone(
    PrunedGenParticleTag  = cms.InputTag("prunedGenParticles"),
    )
    process.LostLepton += process.GenLeptons
    from AllHadronicSUSY.Utils.selectpfcandidates_cfi import SelectPFCandidates
    process.SelectedPFCandidates = SelectPFCandidates.clone(
    PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
    MinPt								  = cms.double(4),
    MaxEta								  = cms.double(5.0),
    )
    process.LostLepton += process.SelectedPFCandidates
    #gamma+jet producers




    #define sequences
    
    #baseline RA2/b variables default shared variables
    RecoCandVector.extend(['LeptonsNew:IdIsoMuon(Muons)','LeptonsNew:IdIsoElectron(Electrons)'])




    ## --- Final paths ----------------------------------------------------

    # put together final sequence with optional producers
    process.AdditionalSequence = cms.Sequence()
    if lostlepton:
      print "Adding LostLepton calculations to final path and tree"
      process.AdditionalSequence += process.LostLepton 
    #  VarsRecoCand = cms.vstring('selectedIDIsoMuons','selectedIDMuons','selectedIDIsoElectrons','selectedIDMuons','IsolatedTracks','HTJets'),
   #   RecoCandVector.extend(['selectedIDIsoMuons','selectedIDMuons','selectedIDIsoElectrons','selectedIDElectrons','IsolatedTracks']),
      RecoCandVector.extend(['IsolatedElectronTracksVeto','IsolatedMuonTracksVeto','IsolatedPionTracksVeto','LeptonsNew:IdIsoMuon(selectedIDIsoMuons)','LeptonsNew:IdMuon(selectedIDMuons)','LeptonsNew:IdIsoElectron(selectedIDIsoElectrons)','LeptonsNew:IdElectron(selectedIDElectrons)','SelectedPFCandidates|SelectedPFCandidates:Charge(I_Charge)|SelectedPFCandidates:Typ(I_Typ)']),
      RecoCandVector.extend(['GenLeptons:Boson(GenBoson)|GenLeptons:BosonPDGId(I_GenBosonPDGId)','GenLeptons:Muon(GenMu)|GenLeptons:MuonTauDecay(I_GenMuFromTau)' ,'GenLeptons:Electron(GenElec)|GenLeptons:ElectronTauDecay(I_GenElecFromTau)','GenLeptons:Tau(GenTau)|GenLeptons:TauHadronic(I_GenTauHad)'] ) # gen information on leptons
      RecoCandVector.extend(['LeptonsNewTag:IdIsoMuon(selectedIDIsoMuonsNoMiniIso)','LeptonsNewTag:IdIsoElectron(selectedIDIsoElectronsNoMiniIso)'] ) # gen information on leptons
      RecoCandVector.extend(['JetsProperties(Jets)|JetsProperties:bDiscriminatorUser(F_bDiscriminator)|JetsProperties:chargedEmEnergyFraction(F_chargedEmEnergyFraction)|JetsProperties:chargedHadronEnergyFraction(F_chargedHadronEnergyFraction)|JetsProperties:chargedHadronMultiplicity(I_chargedHadronMultiplicity)|JetsProperties:electronMultiplicity(I_electronMultiplicity)|JetsProperties:jetArea(F_jetArea)|JetsProperties:muonEnergyFraction(F_muonEnergyFraction)|JetsProperties:muonMultiplicity(I_muonMultiplicity)|JetsProperties:neutralEmEnergyFraction(F_neutralEmEnergyFraction)|JetsProperties:neutralHadronMultiplicity(I_neutralHadronMultiplicity)|JetsProperties:photonEnergyFraction(F_photonEnergyFraction)|JetsProperties:photonMultiplicity(I)'] ) # jet information on various variables
      RecoCandVector.extend(['slimmedElectrons','slimmedMuons'])

    if gammajets:
      print "Adding Gamma+Jet calculations to final path and tree"
      process.AdditionalSequence += process.GammaJet 
    # configure treemaker
    from AllHadronicSUSY.TreeMaker.treeMaker import TreeMaker
    process.TreeMaker2 = TreeMaker.clone(
    	TreeName          = cms.string("PreSelection"),
    	VarsRecoCand = RecoCandVector, 
    	VarsDouble  	  = VarsDouble,
    	VarsInt = VarsInt,
    	VarsBool = VarsBool,
	VectorString = VectorString
	VectorString = VectorString
    	)
    process.dump = cms.EDAnalyzer("EventContentAnalyzer")
    #tag and probe
    if tagandprobe:
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

### begin Zinv stuff ###
    if doZinv:   
   
      process.ZinvClean = cms.Sequence()

      from AllHadronicSUSY.Utils.zproducer_cfi import ZProducer
      process.maketheZs = ZProducer.clone(
         ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
         MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon')
      )
      process.ZinvClean += process.maketheZs
      VarsInt.extend(['maketheZs:ZNum'])
      process.TreeMaker2.VectorTLorentzVector.append("maketheZs:Zp4")

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

      from AllHadronicSUSY.Utils.mhtdouble_cfi import mhtdouble
      process.MHTclean = mhtdouble.clone(
         JetTag = cms.InputTag('MHTJetsclean'),
      )
      process.ZinvClean += process.MHTclean
      VarsDouble.extend(['MHTclean'])

      from AllHadronicSUSY.Utils.metdouble_cfi import metdouble
      process.METclean = metdouble.clone(
         METTag = cms.InputTag("slimmedMETs"),
         JetTag = cms.InputTag('HTJetsclean'),
         cleanTag = cms.untracked.VInputTag(cms.InputTag('LeptonsNew:IdIsoElectron'), cms.InputTag('LeptonsNew:IdIsoMuon'), cms.InputTag('goodPhotons', 'bestPhoton'))
      )
      process.ZinvClean += process.METclean
      VarsDouble.extend(['METclean:minDeltaPhiN(minDeltaPhiNclean)', 'METclean:Pt(METPtclean)'])

      process.AdditionalSequence += process.ZinvClean
### end Zinv stuff ###

    process.WriteTree = cms.Path(
      process.Baseline *
      process.AdditionalSequence *
      #process.dump *
    	process.TreeMaker2
    )

