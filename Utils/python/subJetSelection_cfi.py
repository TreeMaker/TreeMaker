import FWCore.ParameterSet.Config as cms

SubJetSelection = cms.EDProducer('SubJetSelection',
    JetTag = cms.InputTag('slimmedJets'),
    MinPt = cms.double(30),
    MaxEta = cms.double(5.0),
    VetoMaxPt = cms.double(-1),
    VetoMinEta = cms.double(-1),
    VetoMaxEta = cms.double(-1),
    VetoRawPt = cms.bool(False),
    veto = cms.bool(False),
)

SubGenJetSelection = cms.EDProducer('SubGenJetSelection',
    JetTag = cms.InputTag('slimmedGenJets'),
    MinPt = cms.double(30),
    MaxEta = cms.double(5.0),
    VetoMaxPt = cms.double(-1),
    VetoMinEta = cms.double(-1),
    VetoMaxEta = cms.double(-1),
    VetoRawPt = cms.bool(False),
    veto = cms.bool(False),
)
