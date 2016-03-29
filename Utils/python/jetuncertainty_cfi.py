import FWCore.ParameterSet.Config as cms

JetUncertaintyProducer = cms.EDProducer('JetUncertaintyProducer',
   JetTag  = cms.InputTag('slimmedJets'),
   JetType = cms.string('AK4PFchs'),
   jecUncDir = cms.int32(0),
)

