import FWCore.ParameterSet.Config as cms

primaryvertices = cms.EDProducer('PrimaryVerticesProducer',
    VertexCollection     = cms.InputTag('offlineSlimmedPrimaryVertices'),
    GoodVertexCollection = cms.InputTag('goodVertices'),
    saveVertices         = cms.bool(False),
)
