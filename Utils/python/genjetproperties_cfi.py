import FWCore.ParameterSet.Config as cms

genjetproperties = cms.EDProducer('GenJetProperties',
GenJetTag               = cms.InputTag('GenMHTJets')
)
