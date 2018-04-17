import FWCore.ParameterSet.Config as cms

leptonproducer = cms.EDProducer('LeptonProducer',
    MuonTag = cms.InputTag('slimmedMuons'),
    ElectronTag = cms.InputTag('slimmedElectrons'),
    PrimaryVertex = cms.InputTag('offlineSlimmedPrimaryVertices'),
    minElecPt = cms.double(10),
    maxElecEta = cms.double(2.5),
    elecIsoValue = cms.double(0.2), # only has an effect with useMiniIsolation



    minMuPt = cms.double(10),
    maxMuEta = cms.double(2.4),
    muIsoValue = cms.double(0.2),
    muNormalizedChi2Max = cms.double(3.0),
    muChi2LocalPositionMax = cms.double(12.0),
    muTrkKink = cms.double(20.0),
    muValidFractionMin = cms.double(0.8),
    muSegmentCompatibilityMin = cms.vdouble(0.303, 0.451),
    mudBMax = cms.double(0.2), #From loose IP2D
    mudZMax = cms.double(0.5), #From loose IP2D
    tightMuNormalizedChi2Max = cms.double(10.0),
    tightMuNumberOfValidMuonHitsMin = cms.int32(0),
    tightMuNumberOfMatchedStationsMin = cms.int32(1),
    tightMudBMax = cms.double(0.2),
    tightMudZMax = cms.double(0.5),
    tightMuNumberOfValidPixelHitsMin = cms.int32(0),
    tightMuTrackerLayersWithMeasurementMin = cms.int32(5),
    UseMiniIsolation = cms.bool(False),
    METTag = cms.InputTag('slimmedMETs'), 
    rhoCollection = cms.InputTag("fixedGridRhoFastjetAll")
)
