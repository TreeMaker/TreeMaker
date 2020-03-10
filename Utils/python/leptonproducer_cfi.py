import FWCore.ParameterSet.Config as cms

# Electron ID Values From: https://indico.cern.ch/event/732971/contributions/3022843/attachments/1658685/2656462/eleIdTuning.pdf
# Electron EA Values From: https://github.com/cms-sw/cmssw/blob/1fbada01f097fbd446e7a431140f83bc9f5a0ff0/RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt
leptonproducer = cms.EDProducer('LeptonProducer',
    MuonTag                                = cms.InputTag('slimmedMuons'),
    ElectronTag                            = cms.InputTag('slimmedElectrons'),
    PrimaryVertex                          = cms.InputTag('offlineSlimmedPrimaryVertices'),
    minElecPt                              = cms.double(10),
    maxElecEta                             = cms.double(2.5),
    elecIsoValue                           = cms.double(0.2), # only has an effect with useMiniIsolation
    # barrel electrons
    eb_ieta_cut                            = cms.vdouble(0.0126,  0.0112,  0.0106,  0.0104),
    eb_deta_cut                            = cms.vdouble(0.00463, 0.00377, 0.0032,  0.00255),
    eb_dphi_cut                            = cms.vdouble(0.148,   0.0884,  0.0547,  0.022),
    eb_hovere_cut                          = cms.vdouble(0.05,    0.05,    0.046,   0.026),
    eb_hovere_cut2                         = cms.vdouble(1.16,    1.16,    1.16,    1.15),
    eb_hovere_cut3                         = cms.vdouble(0.0324,  0.0324,  0.0324,  0.0324),
    eb_ooeminusoop_cut                     = cms.vdouble(0.209,   0.193,   0.184,   0.159),
    eb_d0_cut                              = cms.vdouble(0.05,    0.05,    0.05,    0.05),
    eb_dz_cut                              = cms.vdouble(0.10,    0.10,    0.10,    0.10),
    eb_misshits_cut                        = cms.vint32 (2,       1,       1,       1),
    # endcap electrons
    ee_ieta_cut                            = cms.vdouble(0.0457,  0.0425,  0.0387,  0.0353),
    ee_deta_cut                            = cms.vdouble(0.00814, 0.00674, 0.00632, 0.00501),
    ee_dphi_cut                            = cms.vdouble(0.19,    0.169,   0.0394,  0.0236),
    ee_hovere_cut                          = cms.vdouble(0.05,    0.0441,  0.0275,  0.0188),
    ee_hovere_cut2                         = cms.vdouble(2.54,    2.54,    2.52,    2.06),
    ee_hovere_cut3                         = cms.vdouble(0.183,   0.183,   0.183,   0.183),
    ee_ooeminusoop_cut                     = cms.vdouble(0.132,   0.111,   0.0721,  0.0197),
    ee_d0_cut                              = cms.vdouble(0.10,    0.10,    0.10,    0.10),
    ee_dz_cut                              = cms.vdouble(0.20,    0.20,    0.20,    0.20),
    ee_misshits_cut                        = cms.vint32 (3,       1,       1,       1),
    # common electrons
    hovere_constant                        = cms.bool(False),
    electronEAValues                       = cms.vdouble(0.1440, 0.1562, 0.1032, 0.0859, 0.1116, 0.1321, 0.1654),
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
