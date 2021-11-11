import FWCore.ParameterSet.Config as cms

candidateTrackFilter = cms.EDFilter('CandidateTrackFilter',
vertexInputTag              = cms.InputTag("goodVertices"),
pfCandidatesTag             = cms.InputTag("packedPFCandidates"),
lostTracksTag               = cms.InputTag("lostTracks"),
lostEleTracksTag            = cms.InputTag("lostTracks","eleTracks"),
doFilter                    = cms.bool(False),
minPt                       = cms.double(1.0),
maxEta                      = cms.double(2.5),
maxdz                       = cms.double(999),
maxdxy                      = cms.double(999),
maxnormchi2                 = cms.double(999),
debug                       = cms.bool(False),
)