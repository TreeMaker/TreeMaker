import FWCore.ParameterSet.Config as cms

GoodJetsProducer = cms.EDFilter('GoodJetsProducer',
    TagMode = cms.bool(False),
    JetTag = cms.InputTag('slimmedJets'),
    maxJetEta = cms.double(5.0),
    minNconstituents = cms.int32(1),
    minNneutrals = cms.int32(10),
    minNcharged = cms.int32(0),
    maxNeutralFraction = cms.double(0.99),
    maxPhotonFraction = cms.double(0.99),
    maxPhotonFractionHF = cms.double(0.90),
    minChargedFraction = cms.double(0),
    maxChargedEMFraction = cms.double(0.99),
    jetPtFilter = cms.double(30.),
    SaveAllJets = cms.bool(False),
    ExcludeLepIsoTrackPhotons = cms.bool(False),
    JetConeSize = cms.double(0.04),
    SkipTag = cms.VInputTag()
)
