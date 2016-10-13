import FWCore.ParameterSet.Config as cms

prescaleweightProducer = cms.EDProducer('PrescaleWeightProducer',

   HLTProcess = cms.string("HLT"),

   PFHTWeights = cms.bool( True ),

   bits = cms.InputTag("TriggerResults","","HLT"),

   prescales = cms.InputTag("patTrigger"),

   objects = cms.InputTag("selectedPatTrigger"),
                                        
)
