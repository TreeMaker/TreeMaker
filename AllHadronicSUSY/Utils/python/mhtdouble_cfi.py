import FWCore.ParameterSet.Config as cms

mhtdouble = cms.EDProducer('MhtDouble',
JetTag_               = cms.InputTag('JetTag'),
)
