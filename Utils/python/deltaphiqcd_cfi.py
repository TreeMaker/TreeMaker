import FWCore.ParameterSet.Config as cms

deltaphiqcd  = cms.EDProducer('DeltaPhiQCD',
JetTagRecoJets = cms.InputTag('GoodJets'),
JetTagGenJets = cms.InputTag('slimmedGenJets'),
BTagInputTag = cms.InputTag('combinedInclusiveSecondaryVertexV2BJetTags'),
GenParticleTag = cms.InputTag('prunedGenParticles'),
GenMETTag  = cms.InputTag('slimmedMETs')
)

