import FWCore.ParameterSet.Config as cms

PDFWeightProducer = cms.EDProducer("PDFWeightProducer",
    storePDFs = cms.bool(True),
    storeScales = cms.bool(True),
    storePSs = cms.bool(True),
    debug = cms.bool(False),
    lheRunTag = cms.InputTag("externalLHEProducer"),
    lheWeightTag = cms.InputTag("lheWeights"),
    genWeightTag = cms.InputTag("genWeights"),
)
