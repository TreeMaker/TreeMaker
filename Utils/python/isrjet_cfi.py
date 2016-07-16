import FWCore.ParameterSet.Config as cms

ISRJetProducer = cms.EDProducer('ISRJetProducer',
    JetTag  = cms.InputTag('slimmedJets'),
    GenPartTag = cms.InputTag('prunedGenParticles'),
    MinPt = cms.double(30),
    MaxEta = cms.double(2.4),
)
