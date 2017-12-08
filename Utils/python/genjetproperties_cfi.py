import FWCore.ParameterSet.Config as cms

genjetproperties = cms.EDProducer('GenJetProperties',
    GenJetTag = cms.InputTag('GenMHTJets'),
    PrunedGenJetTag = cms.InputTag(""),
    SoftDropGenJetTag = cms.InputTag(""),
    distMax = cms.double(0.4),
)
