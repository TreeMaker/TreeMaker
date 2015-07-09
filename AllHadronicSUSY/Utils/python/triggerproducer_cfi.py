import FWCore.ParameterSet.Config as cms

triggerProducer = cms.EDProducer('TriggerProducer',
trigTagArg1  = cms.string('TriggerResults'),
trigTagArg2  = cms.string(''),
trigTagArg3  = cms.string('HLT'),
VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
triggerNameList    =   cms.string("triggerNameList")
)
