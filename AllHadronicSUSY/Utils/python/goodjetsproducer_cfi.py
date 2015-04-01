import FWCore.ParameterSet.Config as cms

GoodJetsProducer = cms.EDProducer('GoodJetsProducer',
JetTag               = cms.InputTag('slimmedJets'),
maxJetEta								  = cms.double(5.0),
maxMuFraction								  = cms.double(2),
minNConstituents								  = cms.double(2),
maxNeutralFraction								  = cms.double(0.99),
maxPhotonFraction								  = cms.double(0.99),
minChargedMultiplicity								  = cms.double(0),
minChargedFraction								  = cms.double(0),
maxChargedEMFraction								  = cms.double(0.99),
)
