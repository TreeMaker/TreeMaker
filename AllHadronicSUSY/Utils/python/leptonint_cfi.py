import FWCore.ParameterSet.Config as cms

leptonint = cms.EDProducer('LeptonInt',
LeptonTag = cms.VInputTag(cms.InputTag('selectedIDIsoMuons'),cms.InputTag('selectedIDIsoElectrons')),
)
