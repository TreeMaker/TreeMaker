import FWCore.ParameterSet.Config as cms

genLeptonRecoCand = cms.EDProducer('GenLeptonRecoCand',
  PrunedGenParticleTag  = cms.InputTag("prunedGenParticles"),
  pfCandTag  = cms.InputTag("packedPFCandidates"),
)
