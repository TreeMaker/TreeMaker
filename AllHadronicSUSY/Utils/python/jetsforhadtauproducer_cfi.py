import FWCore.ParameterSet.Config as cms

JetsForHadTauProducer = cms.EDProducer('JetsForHadTauProducer',
JetTag               = cms.InputTag('slimmedJets'),
reclusJetTag               = cms.InputTag('patJetsAK4PFCHS'),
maxJetEta								  = cms.double(2.4),
maxMuFraction								  = cms.double(2),
minNConstituents								  = cms.double(2),
maxNeutralFraction								  = cms.double(0.99),
maxPhotonFraction								  = cms.double(0.99),
minChargedMultiplicity								  = cms.double(0),
minChargedFraction								  = cms.double(0),
maxChargedEMFraction								  = cms.double(0.99),
jetPtCut_miniAOD=cms.double(10),
genMatch_dR=cms.double(1),
dR_for_xCheck=cms.double(0.2),
relPt_for_xCheck=cms.double(1e-2),
debug=cms.bool(False),
)
