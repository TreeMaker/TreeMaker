import FWCore.ParameterSet.Config as cms

prescaleweightProducer = cms.EDProducer('PrescaleWeightProducer',
   bits = cms.InputTag("TriggerResults","","HLT"),
   prescales = cms.InputTag("patTrigger"),
   prescalesL1min = cms.InputTag("patTrigger:l1min"),
   prescalesL1max = cms.InputTag("patTrigger:l1max"),   
   objects = cms.InputTag("slimmedPatTrigger"),
)
