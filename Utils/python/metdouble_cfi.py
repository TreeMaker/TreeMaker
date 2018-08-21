import FWCore.ParameterSet.Config as cms

metdouble = cms.EDProducer('METDouble',
   METTag  = cms.InputTag("slimmedMETs"),
   GenMETTag  = cms.InputTag("slimmedMETs"),
   JetTag  = cms.InputTag('JetTag'),
   InfTagAK4 = cms.InputTag(''),
   InfTagAK8 = cms.InputTag(''),
)

