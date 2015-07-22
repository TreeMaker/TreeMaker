import FWCore.ParameterSet.Config as cms

genLeptonRecoCand = cms.EDProducer('GenLeptonRecoCand',
  PrunedGenParticleTag  = cms.InputTag("prunedGenParticles"),
)
