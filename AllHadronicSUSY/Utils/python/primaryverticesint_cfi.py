import FWCore.ParameterSet.Config as cms

primaryverticesint = cms.EDProducer('PrimaryVerticesInt',
   VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
)

