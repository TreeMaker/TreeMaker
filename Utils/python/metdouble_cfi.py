import FWCore.ParameterSet.Config as cms

metdouble = cms.EDProducer('METDouble',
   METTag  = cms.InputTag("slimmedMETs"),
   GenMETTag  = cms.InputTag("slimmedMETs"),
   InfTagAK8 = cms.InputTag(''),
)

