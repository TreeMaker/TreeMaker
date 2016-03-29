import FWCore.ParameterSet.Config as cms

jetproperties = cms.EDProducer('JetProperties',
    JetTag       = cms.InputTag('slimmedJets'),
    BTagInputTag = cms.string('combinedSecondaryVertexBJetTags'),
    QGTag        = cms.InputTag("QGTagger","qgLikelihood"),
    AK8          = cms.bool(False)
)
