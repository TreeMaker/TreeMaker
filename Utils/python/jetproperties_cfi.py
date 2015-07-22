import FWCore.ParameterSet.Config as cms

jetproperties = cms.EDProducer('JetProperties',
JetTag_               = cms.InputTag('slimmedJets'),
BTagInputTag	        = cms.string('combinedSecondaryVertexBJetTags'),
)
