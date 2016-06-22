import FWCore.ParameterSet.Config as cms

SusyScanProducer = cms.EDProducer("SusyScanProducer",
    shouldScan = cms.bool(True),
    debug = cms.bool(False),
    is74X = cms.bool(True)
)
