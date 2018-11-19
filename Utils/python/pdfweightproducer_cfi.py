import FWCore.ParameterSet.Config as cms

PDFWeightProducer = cms.EDProducer("PDFWeightProducer",
    nScales = cms.uint32(9),
    nPDFs = cms.uint32(100),
)

from TreeMaker.TreeMaker.TMEras import TMeras
TMeras.TM2017.toModify(PDFWeightProducer,
    nPDFs = 102,
)
