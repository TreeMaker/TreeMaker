import FWCore.ParameterSet.Config as cms

PDFRecalculator = cms.EDProducer("PDFRecalculator",
    normalize = cms.bool(True),
    debug = cms.bool(False),
    recalculatePDFs = cms.bool(False),
    recalculateScales = cms.bool(False),
    nEM = cms.uint32(0),
    nQCD = cms.uint32(0),
    pythiaSettings = cms.vstring(),
    pdfSetName = cms.string(''),
)
