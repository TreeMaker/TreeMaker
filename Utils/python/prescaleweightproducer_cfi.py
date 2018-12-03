import FWCore.ParameterSet.Config as cms

prescaleweightProducer = cms.EDProducer('PrescaleWeightProducer',
   bits = cms.InputTag("TriggerResults","","HLT"),
   prescales = cms.InputTag("patTrigger"),
   prescalesL1min = cms.InputTag("patTrigger:l1min"),
   prescalesL1max = cms.InputTag("patTrigger:l1max"),   
   objects = cms.InputTag("selectedPatTrigger"),
)

from TreeMaker.TreeMaker.TMEras import TMeras
(TMeras.TM2016 & ~TMeras.TM80X).toModify(prescaleweightProducer, objects = cms.InputTag("slimmedPatTrigger"))
(TMeras.TM2017 | TMeras.TM2018).toModify(prescaleweightProducer, objects = cms.InputTag("slimmedPatTrigger"))
