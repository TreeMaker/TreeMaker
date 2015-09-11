import FWCore.ParameterSet.Config as cms

GenJetsProducer = cms.EDProducer('GenJetsProducer',
                                 GenJetsTag = cms.InputTag('slimmedGenJets')
)
