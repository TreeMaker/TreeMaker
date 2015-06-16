import FWCore.ParameterSet.Config as cms

TriggerFlagsProducer = cms.EDProducer('TriggerFlagsProducer',
bits = cms.InputTag("TriggerResults","","PAT")
)
