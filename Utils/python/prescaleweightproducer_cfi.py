import FWCore.ParameterSet.Config as cms

prescaleweightProducer = cms.EDProducer('PrescaleWeightProducer',

   bits = cms.InputTag("TriggerResults","","HLT"),

   prescales = cms.InputTag("patTrigger"),

   objects = cms.InputTag("slimmedPatTrigger"),
)
