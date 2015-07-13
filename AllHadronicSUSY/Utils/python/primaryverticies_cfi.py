import FWCore.ParameterSet.Config as cms

primaryverticies = cms.EDProducer('PrimaryVerticiesInt',
VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
)
