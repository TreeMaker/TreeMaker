import FWCore.ParameterSet.Config as cms

prescaleweightProducer = cms.EDProducer('PrescaleWeightProducer',

   bits = cms.InputTag("TriggerResults","","HLT"),

   prescales = cms.InputTag("patTrigger"),

   objects = cms.InputTag("selectedPatTrigger"),
                                        
)

from TreeMaker.TreeMaker.TMEras import TMeras
TMeras.TM2017.toModify(prescaleweightProducer, objects = cms.InputTag("slimmedPatTrigger"))
