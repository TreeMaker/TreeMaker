import FWCore.ParameterSet.Config as cms

primaryverticies = cms.EDProducer('PrimaryVericiesInt',
VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
)
