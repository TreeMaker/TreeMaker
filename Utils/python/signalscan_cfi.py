import FWCore.ParameterSet.Config as cms

SignalScanProducer = cms.EDProducer("SignalScanProducer",
	signalType = cms.string("None"),
    debug = cms.bool(False),
    isLHE = cms.bool(True),
    genCollection = cms.InputTag("prunedGenParticles"),
    motherPDGID = cms.int32(1000023),
    lspPDGID = cms.int32(1000022),
)
