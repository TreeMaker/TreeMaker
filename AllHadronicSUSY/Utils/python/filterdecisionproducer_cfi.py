import FWCore.ParameterSet.Config as cms

filterDecisionProducer = cms.EDProducer('FilterDecisionProducer',
trigTagArg1  = cms.string('TriggerResults'),
trigTagArg2  = cms.string(''),
trigTagArg3  = cms.string('PAT'),
filterName    =   cms.string("Flag_METFilters")
)
