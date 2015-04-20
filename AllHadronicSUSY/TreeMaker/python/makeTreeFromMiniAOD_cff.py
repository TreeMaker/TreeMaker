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
gammajets=False,
tagandprobe=False,
applybaseline=False):

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
    process.LeptonsNewNoMiniIso = leptonproducer.clone(
      MuonTag = cms.InputTag('slimmedMuons'),
      ElectronTag = cms.InputTag('slimmedElectrons'),
      PrimaryVertex = cms.InputTag('offlineSlimmedPrimaryVertices'),
      minElecPt								  = cms.double(10),
      maxElecEta								  = cms.double(2.5),
      minMuPt								  = cms.double(10),
      maxMuEta								  = cms.double(2.4),
      muIsoValue								  = cms.double(0.2),
      elecIsoValue								  = cms.double(0.2), # only has an effect when used with miniIsolation
      UseMiniIsolation = cms.bool(False),
      )
    process.Baseline += process.LeptonsNewNoMiniIso
    VarsInt.extend(['LeptonsNewNoMiniIso(LeptonsNoMiniIsolation)'])
    from AllHadronicSUSY.Utils.goodjetsproducer_cfi import GoodJetsProducer
    process.GoodJets = GoodJetsProducer.clone(
      JetTag= cms.InputTag('slimmedJets'),
      maxJetEta								  = cms.double(99), #store all jets 
      maxMuFraction								  = cms.double(200), ## effectively no cut if above 1
      minNConstituents								  = cms.double(1),
      maxNeutralFraction								  = cms.double(0.99),
      maxPhotonFraction								  = cms.double(0.99),
      minChargedMultiplicity								  = cms.double(0),
      minChargedFraction								  = cms.double(0),
      maxChargedEMFraction								  = cms.double(0.99),
      )
    from AllHadronicSUSY.Utils.leptontagandprobeproducer_cfi import leptontagandprobeproducer
    process.MuonIsoTagAndProbe = leptontagandprobeproducer.clone(
    	TagPFCand = cms.InputTag('LeptonsNew:IdIsoMuon'),
      ProbePFCand = cms.InputTag('LeptonsNew:IdMuon'),
      ProbeTestPFCand = cms.InputTag('LeptonsNew:IdIsoMuon'),
      JetTag  = cms.InputTag('HTJets'),
      )
    process.MuonIdTagAndProbe = leptontagandprobeproducer.clone(
    	TagPFCand = cms.InputTag('LeptonsNew:IdIsoMuon'),
    	ProbePFCand = cms.InputTag('slimmedMuons'),
    	ProbeTestPFCand = cms.InputTag('LeptonsNew:IdMuon'),
    	JetTag  = cms.InputTag('HTJets'),
      )
    process.ElectronIsoTagAndProbe = leptontagandprobeproducer.clone(
    	TagPFCand = cms.InputTag('LeptonsNew:IdIsoElectron'),
      ProbePFCand = cms.InputTag('LeptonsNew:IdElectron'),
      ProbeTestPFCand = cms.InputTag('LeptonsNew:IdIsoElectron'),
      JetTag  = cms.InputTag('HTJets'),
      )
    process.ElectronIdTagAndProbe = leptontagandprobeproducer.clone(
    	TagPFCand = cms.InputTag('LeptonsNew:IdIsoElectron'),
    	ProbePFCand = cms.InputTag('slimmedElectrons'),
    	ProbeTestPFCand = cms.InputTag('LeptonsNew:IdElectron'),
    	JetTag  = cms.InputTag('HTJets'),
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


    #tag and probe
    if tagandprobe:
			process.Baseline += process.GenLeptons
			process.Baseline += process.JetsProperties
			process.Baseline += process.SelectedPFCandidates
			process.Baseline += process.MuonIsoTagAndProbe
			RecoCandVector.extend(['MuonIsoTagAndProbe:Tag(TagIsoMuon)','MuonIsoTagAndProbe:Probe(ProbeIsoMuon)|MuonIsoTagAndProbe:InvariantMass(F_InvariantMass)|MuonIsoTagAndProbe:PassingOrFail(I_PassingOrFail)'])
			VarsDouble.extend(['MuonIsoTagAndProbe:MinDeltaPhiN(MuIso_minDeltaPhiN)'])
			process.Baseline += process.MuonIdTagAndProbe
			RecoCandVector.extend(['MuonIdTagAndProbe:Tag(TagIDMuon)','MuonIdTagAndProbe:Probe(ProbeIDMuon)|MuonIdTagAndProbe:InvariantMass(F_InvariantMass)|MuonIdTagAndProbe:PassingOrFail(I_PassingOrFail)'])
			VarsDouble.extend(['MuonIdTagAndProbe:MinDeltaPhiN(MuID_minDeltaPhiN)'])
			process.Baseline += process.ElectronIsoTagAndProbe
			RecoCandVector.extend(['ElectronIsoTagAndProbe:Tag(TagIsoElectron)','ElectronIsoTagAndProbe:Probe(ProbeIsoElectron)|ElectronIsoTagAndProbe:InvariantMass(F_InvariantMass)|ElectronIsoTagAndProbe:PassingOrFail(I_PassingOrFail)'])
			VarsDouble.extend(['ElectronIsoTagAndProbe:MinDeltaPhiN(ElecIso_minDeltaPhiN)'])
			process.Baseline += process.ElectronIdTagAndProbe
			RecoCandVector.extend(['ElectronIdTagAndProbe:Tag(TagIDElectron)','ElectronIdTagAndProbe:Probe(ProbeIDElectron)|ElectronIdTagAndProbe:InvariantMass(F_InvariantMass)|ElectronIdTagAndProbe:PassingOrFail(I_PassingOrFail)'])
			VarsDouble.extend(['ElectronIdTagAndProbe:MinDeltaPhiN(ElecID_minDeltaPhiN)'])
			RecoCandVector.extend(['JetsProperties(Jets)|JetsProperties:bDiscriminator(F_bDiscriminator)|JetsProperties:chargedEmEnergyFraction(F_chargedEmEnergyFraction)|JetsProperties:chargedHadronEnergyFraction(F_chargedHadronEnergyFraction)|JetsProperties:chargedHadronMultiplicity(I_chargedHadronMultiplicity)|JetsProperties:electronMultiplicity(I_electronMultiplicity)|JetsProperties:jetArea(F_jetArea)|JetsProperties:muonEnergyFraction(F_muonEnergyFraction)|JetsProperties:muonMultiplicity(I_muonMultiplicity)|JetsProperties:neutralEmEnergyFraction(F_neutralEmEnergyFraction)|JetsProperties:neutralHadronMultiplicity(I_neutralHadronMultiplicity)|JetsProperties:photonEnergyFraction(F_photonEnergyFraction)|JetsProperties:photonMultiplicity(I)','SelectedPFCandidates|SelectedPFCandidates:Charge(I_Charge)|SelectedPFCandidates:Typ(I_Typ)'] ) # jet
			RecoCandVector.extend(['GenLeptons:Boson(GenBoson)|GenLeptons:BosonPDGId(I_GenBosonPDGId)','GenLeptons:Muon(GenMu)|GenLeptons:MuonTauDecay(I_GenMuFromTau)' ,'GenLeptons:Electron(GenElec)|GenLeptons:ElectronTauDecay(I_GenElecFromTau)','GenLeptons:Tau(GenTau)|GenLeptons:TauHadronic(I_GenTauHad)'] )
			RecoCandVector.extend(['IsolatedTracks','LeptonsNew:IdIsoMuon(selectedIDIsoMuons)','LeptonsNew:IdMuon(selectedIDMuons)','LeptonsNew:IdIsoElectron(selectedIDIsoElectrons)','LeptonsNew:IdElectron(selectedIDElectrons)','SelectedPFCandidates|SelectedPFCandidates:Charge(I_Charge)|SelectedPFCandidates:Typ(I_Typ)']),
			

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
      RecoCandVector.extend(['LeptonsNewNoMiniIso:IdIsoMuon(selectedIDIsoMuonsNoMiniIso)','LeptonsNewNoMiniIso:IdIsoElectron(selectedIDIsoElectronsNoMiniIso)'] ) # gen information on leptons
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
    	#process.dump *
    	process.TreeMaker2

        )
