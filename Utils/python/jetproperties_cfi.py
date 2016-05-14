import FWCore.ParameterSet.Config as cms

jetproperties = cms.EDProducer('JetProperties',
    JetTag       = cms.InputTag('slimmedJets'),
    BTagInputTag = cms.string('combinedSecondaryVertexBJetTags'),
    QGTag        = cms.InputTag("QGTagger","qgLikelihood"),
    QGTagMult = cms.InputTag("QGTagger","mult"),
    QGTagPtD = cms.InputTag("QGTagger","ptD"),
    QGTagAxis2 = cms.InputTag("QGTagger","axis2"),
    AK8          = cms.bool(False)
)
