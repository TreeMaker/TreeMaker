import FWCore.ParameterSet.Config as cms

SmearedPATJetProducer = cms.EDProducer("SmearedPATJetProducer",
    src = cms.InputTag("slimmedJets"),
    enabled = cms.bool(True),
    store_factor = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    skipGenMatching = cms.bool(False),
    # Read from GT
    algopt = cms.string('AK4PFchs_pt'),
    algo = cms.string('AK4PFchs'),
    # Gen jet matching
    genJets = cms.InputTag("slimmedGenJets"),
    dRMax = cms.double(0.2),
    dPtMaxFactor = cms.double(3),
    variation = cms.int32(0),
    seed = cms.uint32(37428479),
)