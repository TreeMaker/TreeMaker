import FWCore.ParameterSet.Config as cms

candidateTrackFilter = cms.EDFilter('CandidateTrackFilter',
vertexInputTag  = cms.InputTag("goodVertices"),
pfCandidatesTag = cms.InputTag("packedPFCandidates"),
minPt           = cms.double(0.5),
maxEta          = cms.double(2.5),
maxdz           = cms.double(999),
maxdxy          = cms.double(999),
maxnormchi2     = cms.double(999),
debug           = cms.bool(False),
)

from TreeMaker.TreeMaker.TMEras import TMeras
TMeras.TM80X.toModify(candidateTrackFilter, minPt = cms.double(0.95))

# In 2016, only PFCandidates with pT>0.95 GeV had additional track information saved.
# In 2017 and beyond the extra information was saved for PFCandidates with pT>0.5 GeV, but at a reduced precision between 0.5<pT<0.95 GeV.
# Save only events with a good PV
# Save all tracks, even those without a charge.
# Skip a PF candidate if it doesn't have the associated track information