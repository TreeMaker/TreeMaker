import FWCore.ParameterSet.Config as cms

metdouble = cms.EDProducer('METDouble',
   METTag  = cms.InputTag("slimmedMETs"),
   JetTag  = cms.InputTag('JetTag'),
   cleanTag = cms.untracked.VInputTag()
)

