# $Id: makeTreeFromPAT_cff.py,v 1.16 2013/01/24 15:42:53 mschrode Exp $
#

import FWCore.ParameterSet.Config as cms

def makeTreeTreeFromMiniADO(process,
outFileName,
reportEveryEvt=10,
testFileName="",
Global_Tag="",
numProcessedEvt=1000,
lostlepton=False,
gammajets=False):

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
    from AllHadronicSUSY.Utils.primaryverticies_cfi import primaryverticies
    process.NVtx = primaryverticies.clone(
    VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    )
    process.Baseline += process.NVtx
    VarsInt.extend(['NVtx'])
    ## isotrack producer
    from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationFilter
    from AllHadronicSUSY.Utils.trackIsolationMaker_cfi import trackIsolationCounter
    process.IsolatedTracks = trackIsolationFilter.clone(
      doTrkIsoVeto= False,
      vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
      pfCandidatesTag = cms.InputTag("packedPFCandidates"),
      dR_ConeSize         = cms.double(0.3),
      dz_CutValue         = cms.double(0.05),
      minPt_PFCandidate   = cms.double(10.0),
      isoCut              = cms.double(0.1),
      mTCut=cms.double(-1.),
      )
    process.LostLepton += process.IsolatedTracks
    process.IsolatedTracksVeto = trackIsolationFilter.clone(
    doTrkIsoVeto= False,
    vertexInputTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    pfCandidatesTag = cms.InputTag("packedPFCandidates"),
    dR_ConeSize         = cms.double(0.3),
    dz_CutValue         = cms.double(0.05),
    minPt_PFCandidate   = cms.double(15.0),
    isoCut              = cms.double(0.1),
    mTCut=cms.double(100.),
    )
    process.Baseline += process.IsolatedTracksVeto
    VarsInt.extend(['IsolatedTracksVeto:isoTracks'])
    #process.load("PhysicsTools.PatAlgos.selectionLayer1.muonCountFilter_cfi")
    #process.load("PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi")
    #process.selectedIDIsoMuons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedMuons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
    #(pfIsolationR04().sumChargedHadronPt+
    #max(0.,pfIsolationR04().sumNeutralHadronEt+
    #pfIsolationR04().sumPhotonEt-
    #0.50*pfIsolationR04().sumPUPt))/pt < 0.20 &&
    #(isPFMuon && (isGlobalMuon || isTrackerMuon) )'''))
    #process.Baseline += process.selectedIDIsoMuons
    #process.selectedIDMuons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedMuons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
    #(isPFMuon && (isGlobalMuon || isTrackerMuon) )'''))
    #process.LostLepton += process.selectedIDMuons
    #process.selectedIDIsoElectrons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedElectrons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
    #gsfTrack.isAvailable() &&
    #gsfTrack.hitPattern().numberOfLostHits('MISSING_INNER_HITS')<2 &&
    #(pfIsolationVariables().sumChargedHadronPt+
    #max(0.,pfIsolationVariables().sumNeutralHadronEt+
    #pfIsolationVariables().sumPhotonEt-
    #0.5*pfIsolationVariables().sumPUPt))/pt < 0.20'''))
    #process.Baseline += process.selectedIDIsoElectrons
    #process.selectedIDElectrons = cms.EDFilter("CandPtrSelector", src = cms.InputTag("slimmedElectrons"), cut = cms.string('''abs(eta)<2.5 && pt>10. &&
    #gsfTrack.isAvailable() &&
    #gsfTrack.hitPattern().numberOfLostHits('MISSING_INNER_HITS')<2'''))
    #process.LostLepton += process.selectedIDElectrons
    #from AllHadronicSUSY.Utils.leptonint_cfi import leptonint
    #process.Leptons = leptonint.clone(
    #LeptonTag = cms.VInputTag(cms.InputTag('selectedIDIsoMuons'),cms.InputTag('selectedIDIsoElectrons')),
    #)
    #process.Baseline += process.Leptons
    #VarsInt.extend(['Leptons(LeptonsOld)'])
    from AllHadronicSUSY.Utils.leptonproducer_cfi import leptonproducer
    process.LeptonsNew = leptonproducer.clone(
      MuonTag = cms.InputTag('slimmedMuons'),
      ElectronTag = cms.InputTag('slimmedElectrons'),
      PrimaryVertex = cms.InputTag('offlineSlimmedPrimaryVertices'),
      minElecPt								  = cms.double(5),
      maxElecEta								  = cms.double(2.5),
      minMuPt								  = cms.double(5),
      maxMuEta								  = cms.double(2.4),
      )
    process.Baseline += process.LeptonsNew
    VarsInt.extend(['LeptonsNew(Leptons)'])
    from AllHadronicSUSY.Utils.goodjetsproducer_cfi import GoodJetsProducer
    process.GoodJets = GoodJetsProducer.clone(
      JetTag= cms.InputTag('slimmedJets'),
      maxMuFraction								  = cms.double(0.99),
      minNConstituents								  = cms.double(1),
      maxNeutralFraction								  = cms.double(0.99),
      maxPhotonFraction								  = cms.double(0.99),
      minChargedMultiplicity								  = cms.double(0),
      minChargedFraction								  = cms.double(0),
      maxChargedEMFraction								  = cms.double(0.99),
      )
    process.Baseline += process.GoodJets
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
    JetTag  = cms.InputTag('GoodJets'),
    BTagInputTag	        = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
    METTag  = cms.InputTag("slimmedMETs"),
    )
    process.LostLepton += process.JetsProperties
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
      RecoCandVector.extend(['IsolatedTracks','LeptonsNew:IdIsoMuon(selectedIDIsoMuons)','LeptonsNew:IdMuon(selectedIDMuons)','LeptonsNew:IdIsoElectron(selectedIDIsoElectrons)','LeptonsNew:IdElectron(selectedIDElectrons)','SelectedPFCandidates|SelectedPFCandidates:Charge(I_Charge)|SelectedPFCandidates:Typ(I_Typ)']),
      RecoCandVector.extend(['GenLeptons:Boson(GenBoson)|GenLeptons:BosonPDGId(I_GenBosonPDGId)','GenLeptons:Muon(GenMu)|GenLeptons:MuonTauDecay(I_GenMuFromTau)' ,'GenLeptons:Electron(GenElec)|GenLeptons:ElectronTauDecay(I_GenElecFromTau)','GenLeptons:Tau(GenTau)|GenLeptons:TauHadronic(I_GenTauHad)'] ) # gen information on leptons
      RecoCandVector.extend(['JetsProperties(Jets)|JetsProperties:bDiscriminator(F_bDiscriminator)|JetsProperties:chargedEmEnergyFraction(F_chargedEmEnergyFraction)|JetsProperties:chargedHadronEnergyFraction(F_chargedHadronEnergyFraction)|JetsProperties:chargedHadronMultiplicity(I_chargedHadronMultiplicity)|JetsProperties:electronMultiplicity(I_electronMultiplicity)|JetsProperties:jetArea(F_jetArea)|JetsProperties:muonEnergyFraction(F_muonEnergyFraction)|JetsProperties:muonMultiplicity(I_muonMultiplicity)|JetsProperties:neutralEmEnergyFraction(F_neutralEmEnergyFraction)|JetsProperties:neutralHadronMultiplicity(I_neutralHadronMultiplicity)|JetsProperties:photonEnergyFraction(F_photonEnergyFraction)|JetsProperties:photonMultiplicity(I)'] ) # jet information on various variables

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
    	)
    process.dump = cms.EDAnalyzer("EventContentAnalyzer")
    process.WriteTree = cms.Path(
        process.Baseline *
        process.AdditionalSequence *
   # 	process.dump *
    	process.TreeMaker2

        )
