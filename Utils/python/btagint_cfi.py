import FWCore.ParameterSet.Config as cms

btagint = cms.EDProducer('BTagInt',
JetTag_               = cms.InputTag('JetTag'),
BTagInputTag	        = cms.string('combinedSecondaryVertexBJetTags'),
BTagCutValue					= cms.double(0.679)
)
