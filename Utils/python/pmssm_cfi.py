import FWCore.ParameterSet.Config as cms

PmssmProducer = cms.EDProducer("PmssmProducer",
    shouldScan = cms.bool(True),
    debug = cms.bool(False)
)
