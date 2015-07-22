import FWCore.ParameterSet.Config as cms

deltaphidouble = cms.EDProducer('DeltaPhiDouble',
DeltaPhiJets  = cms.InputTag("HTJets"),
MHTJets  = cms.InputTag("MHTJets"),
)
