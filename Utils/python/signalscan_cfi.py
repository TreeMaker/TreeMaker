import FWCore.ParameterSet.Config as cms

SignalScanProducer = cms.EDProducer("SignalScanProducer",
	signalType = cms.string("None"),
    debug = cms.bool(False),
    isLHE = cms.bool(True)
)
