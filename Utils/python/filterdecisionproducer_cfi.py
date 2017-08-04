import FWCore.ParameterSet.Config as cms

filterDecisionProducer = cms.EDProducer('FilterDecisionProducer',
trigTagArg1  = cms.string('slimmedPatTrigger'),
trigTagArg2  = cms.string('filterLabels'),
trigTagArg3  = cms.string(''),
filterName    =   cms.string("Flag_METFilters")
)
