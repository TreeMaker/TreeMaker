import FWCore.ParameterSet.Config as cms

# UL2017 medium WP as default
btagint = cms.EDProducer('BTagInt',
JetTag_               = cms.InputTag('JetTag'),
BTagInputTag	        = cms.string('pfDeepCSVDiscriminatorsJetTags:BvsAll'),
BTagCutValue					= cms.double(0.4506)
)
