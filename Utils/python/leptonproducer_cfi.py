import FWCore.ParameterSet.Config as cms

leptonproducer = cms.EDProducer('LeptonProducer',
    MuonTag                                = cms.InputTag('slimmedMuons'),
    ElectronTag                            = cms.InputTag('slimmedElectrons'),
    PrimaryVertex                          = cms.InputTag('offlineSlimmedPrimaryVertices'),
    minElecPt                              = cms.double(10),
    maxElecEta                             = cms.double(2.5),
    elecIsoValue                           = cms.double(0.2), # only has an effect with useMiniIsolation
    # barrel electrons
    eb_ieta_cut                            = cms.vdouble(0.0115,  0.011,   0.00998, 0.00998),
    eb_deta_cut                            = cms.vdouble(0.00749, 0.00477, 0.00311, 0.00308),
    eb_dphi_cut                            = cms.vdouble(0.228,   0.222,   0.103,   0.0816),
    eb_hovere_cut                          = cms.vdouble(0.356,   0.298,   0.253,   0.0414),
    eb_hovere_parameters                   = cms.vdouble(1.12,    0.0368),
    eb_ooeminusoop_cut                     = cms.vdouble(0.299,   0.241,   0.134,   0.0129),
    eb_d0_cut                              = cms.vdouble(0.05,    0.05,    0.05,    0.05),
    eb_dz_cut                              = cms.vdouble(0.10,    0.10,    0.10,    0.10),
    eb_misshits_cut                        = cms.vint32 (2,       1,       1,       1),
    # endcap electrons
    ee_ieta_cut                            = cms.vdouble(0.037,   0.0314,  0.0298,  0.0292),
    ee_deta_cut                            = cms.vdouble(0.00895, 0.00868, 0.00609, 0.00605),
    ee_dphi_cut                            = cms.vdouble(0.213,   0.213,   0.045,   0.0394),
    ee_hovere_cut                          = cms.vdouble(0.211,   0.101,   0.0878,  0.0641),
    ee_hovere_parameters                   = cms.vdouble(0.5,     0.201),
    ee_ooeminusoop_cut                     = cms.vdouble(0.15,    0.14,    0.13,    0.0129),
    ee_d0_cut                              = cms.vdouble(0.10,    0.10,    0.10,    0.10),
    ee_dz_cut                              = cms.vdouble(0.20,    0.20,    0.20,    0.20),
    ee_misshits_cut                        = cms.vint32 (3,       1,       1,       1),
    # common electrons
    hovere_constant                        = cms.bool(True),
    electronEAValues                       = cms.vdouble(0.1752, 0.1862, 0.1411, 0.1534, 0.1903, 0.2243, 0.2687),
    #muons
    minMuPt                                = cms.double(10),
    maxMuEta                               = cms.double(2.4),
    muIsoValue                             = cms.double(0.2), #loose (<0.40), medium (<0.20), tight (<0.10), very tight (<0.05)
    muonEAValues                           = cms.vdouble(0.0735, 0.0619, 0.0465, 0.0433, 0.0577),
    muNormalizedChi2Max                    = cms.double(3.0),
    muChi2LocalPositionMax                 = cms.double(12.0),
    muTrkKink                              = cms.double(20.0),
    muValidFractionMin                     = cms.double(0.8),
    muSegmentCompatibilityMin              = cms.vdouble(0.303, 0.451),
    mudBMax                                = cms.double(0.2), #From loose IP2D
    mudZMax                                = cms.double(0.5), #From loose IP2D
    tightMuNormalizedChi2Max               = cms.double(10.0),
    tightMuNumberOfValidMuonHitsMin        = cms.int32(0),
    tightMuNumberOfMatchedStationsMin      = cms.int32(1),
    tightMudBMax                           = cms.double(0.2),
    tightMudZMax                           = cms.double(0.5),
    tightMuNumberOfValidPixelHitsMin       = cms.int32(0),
    tightMuTrackerLayersWithMeasurementMin = cms.int32(5),
    UseMiniIsolation                       = cms.bool(False),
    METTag                                 = cms.InputTag('slimmedMETs'), 
    rhoCollection                          = cms.InputTag("fixedGridRhoFastjetAll")
)
