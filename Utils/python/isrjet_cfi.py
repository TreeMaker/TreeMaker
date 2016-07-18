import FWCore.ParameterSet.Config as cms

ISRJetProducer = cms.EDProducer('ISRJetProducer',
    JetTag  = cms.InputTag('slimmedJets'),
    JetLeptonTag  = cms.InputTag('GoodJets:JetLeptonMask'),
    GenPartTag = cms.InputTag('prunedGenParticles'),
    MinPt = cms.double(30),
    MaxEta = cms.double(2.4),
)
