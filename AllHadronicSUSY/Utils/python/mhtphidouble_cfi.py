import FWCore.ParameterSet.Config as cms

mhtphidouble = cms.EDProducer('MhtPhiDouble',
JetTag_               = cms.InputTag('JetTag'),
)
