import FWCore.ParameterSet.Config as cms

njetint = cms.EDProducer('NJetInt',
JetTag_               = cms.InputTag('JetTag'),
)
