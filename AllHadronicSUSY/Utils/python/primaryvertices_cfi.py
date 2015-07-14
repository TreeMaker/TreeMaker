import FWCore.ParameterSet.Config as cms

primaryvertices = cms.EDProducer('PrimaryVerticesInt',
VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
)
