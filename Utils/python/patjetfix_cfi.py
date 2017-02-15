import FWCore.ParameterSet.Config as cms

patjetfix = cms.EDProducer('PatJetFix',
    electronsFixed = cms.InputTag("slimmedElectrons"),
    photonsFixed = cms.InputTag("slimmedPhotons"),
    electrons = cms.InputTag("slimmedElectronsBeforeGSFix"),
    PackedPart = cms.InputTag("packedPFCandidates"),
    METCorr = cms.InputTag("slimmedMETsEGClean"),
    MET = cms.InputTag("slimmedMETsUncorrected"),
    photons = cms.InputTag("slimmedPhotonsBeforeGSFix"),
    jets = cms.InputTag("slimmedJets"),
)
