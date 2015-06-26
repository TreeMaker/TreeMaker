import FWCore.ParameterSet.Config as cms

trackIsolationFilter = cms.EDFilter("TrackIsolationFilter",
                                     pfCandidatesTag     = cms.InputTag("particleFlow"),
                                     vertexInputTag      = cms.InputTag("goodVertices"),
				     METTag  = cms.InputTag("slimmedMETs"), 
                                     dR_ConeSize         = cms.double(0.3),
                                     dz_CutValue         = cms.double(0.1),
                                     minPt_PFCandidate   = cms.double(15.0),
                                     isoCut              = cms.double(0.1),
                                     doTrkIsoVeto        = cms.bool(True),
                                     pdgId               = cms.int32(0),
				     etaCut=cms.double(2.5),
				     mTCut=cms.double(100.),
)

trackIsolationCounter  = cms.EDFilter("PATCandViewCountFilter",
                                      minNumber = cms.uint32(0),
                                      maxNumber = cms.uint32(999999),
                                      src = cms.InputTag("trackIsolationFilter")
)

