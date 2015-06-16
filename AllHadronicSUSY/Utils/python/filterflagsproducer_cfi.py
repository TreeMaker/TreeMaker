import FWCore.ParameterSet.Config as cms

FilterFlagsProducer = cms.EDProducer('FilterFlagsProducer',
bits = cms.InputTag("TriggerResults","","PAT")
)
