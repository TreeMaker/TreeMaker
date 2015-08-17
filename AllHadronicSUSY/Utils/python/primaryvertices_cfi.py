import FWCore.ParameterSet.Config as cms

primaryvertices = cms.EDProducer('PrimaryVerticesInt',
VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
checkFake     = cms.bool(True),
maxVertexNdof = cms.int32(4),
maxVertexZ    = cms.double(24.),
maxVertexRho  = cms.double(2.)
)
