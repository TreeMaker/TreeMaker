import FWCore.ParameterSet.Config as cms

PDFWeightProducer = cms.EDProducer("PDFWeightProducer",
    nScales = cms.uint32(9),
    nPDFs = cms.uint32(100),
    nPSs = cms.uint32(14),
    normalize = cms.bool(True),
)

from TreeMaker.TreeMaker.TMEras import TMeras
(TMeras.TMUL2017 | TMeras.TMUL2018).toModify(PDFWeightProducer,
    nPDFs = 102,
)
