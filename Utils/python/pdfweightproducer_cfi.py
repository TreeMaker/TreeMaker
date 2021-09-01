import FWCore.ParameterSet.Config as cms

PDFWeightProducer = cms.EDProducer("PDFWeightProducer",
    nScales = cms.uint32(9),
    nPDFs = cms.uint32(100),
    nPSs = cms.uint32(14),
    nQCD = cms.uint32(0),
    nEM = cms.uint32(0),
    normalize = cms.bool(True),
    pythiaSettings = cms.vstring(),
)

from TreeMaker.TreeMaker.TMEras import TMeras
(TMeras.TM2017 | TMeras.TM2018).toModify(PDFWeightProducer,
    nPDFs = 102,
)
