import FWCore.ParameterSet.Config as cms

triggerProducer = cms.EDProducer('TriggerProducer',
trigTagArg1  = cms.string('TriggerResults'),
trigTagArg2  = cms.string(''),
trigTagArg3  = cms.string('HLT'),
prescaleTagArg1  = cms.string('patTrigger'),
prescaleTagArg2  = cms.string(''),
prescaleTagArg3  = cms.string(''),
VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
saveHLTObj = cms.bool(False),
triggerNameList    =   cms.vstring()
)
