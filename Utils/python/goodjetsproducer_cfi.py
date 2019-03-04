import FWCore.ParameterSet.Config as cms

GoodJetsProducer = cms.EDFilter('GoodJetsProducer',
    TagMode = cms.bool(False),
    JetTag = cms.InputTag('slimmedJets'),
    maxJetEta = cms.double(5.0),

    #available varnames are (abbrev=full):
    #   nef=neutralEmEnergyFraction
    #   nhf=neutralHadronEnergyFraction
    #   nm=neutralMultiplicity
    #   cef=chargedEmEnergyFraction
    #   chf=chargedHadronEnergyFraction
    #   cm=chargedMultiplicity
    #   nc=nconstituents
    #   mf=muonEnergyFraction
    varnames  = cms.vstring('nhf','nef','nc','chf','cm','cef','nef','nhf','nm','nef','nm'),
    etamin    = cms.vdouble( -1.0, -1.0,-1.0, -1.0,-1.0, -1.0,  2.7,  2.7, 2.7,  3.0, 3.0),
    etamax    = cms.vdouble(  2.7,  2.7, 2.7,  2.4, 2.4,  2.4,  3.0,  3.0, 3.0, -1.0,-1.0),
    cutvalmin = cms.vdouble( -1.0, -1.0, 1.0,  0.0, 0.0, -1.0, 0.01, -1.0, 2.0, -1.0,10.0),
    cutvalmax = cms.vdouble( 0.99, 0.99,-1.0, -1.0,-1.0, 0.99, -1.0, 0.98,-1.0, 0.90,-1.0),

    jetPtFilter = cms.double(30.),
    invertJetPtFilter = cms.bool(False),
    SaveAllJetsId = cms.bool(False),
    SaveAllJetsPt = cms.bool(False),
    ExcludeLepIsoTrackPhotons = cms.bool(False),
    JetConeSize = cms.double(0.04),
    SkipTag = cms.VInputTag()
)

from TreeMaker.TreeMaker.TMEras import TMeras
TMeras.TM2017.toModify(GoodJetsProducer,
    varnames  = cms.vstring('nhf','nef','nc','chf','cm','nef','nm','nef','nhf','nm'),
    etamin    = cms.vdouble( -1.0, -1.0,-1.0, -1.0,-1.0,  2.7, 2.7,  3.0,  3.0, 3.0),
    etamax    = cms.vdouble(  2.7,  2.7, 2.7,  2.4, 2.4,  3.0, 3.0, -1.0, -1.0,-1.0),
    cutvalmin = cms.vdouble( -1.0, -1.0, 1.0,  0.0, 0.0, 0.02, 2.0, -1.0, 0.02,10.0),
    cutvalmax = cms.vdouble( 0.90, 0.90,-1.0, -1.0,-1.0, 0.99,-1.0, 0.90, -1.0,-1.0),
)
TMeras.TM2018.toModify(GoodJetsProducer,
    varnames  = cms.vstring('nhf','nef','nc','chf','cm','nhf','nef','cm','nef','nm','nef','nhf','nm'),
    etamin    = cms.vdouble( -1.0, -1.0,-1.0, -1.0,-1.0,  2.6,  2.6, 2.6,  2.7, 2.7,  3.0,  3.0, 3.0),
    etamax    = cms.vdouble(  2.6,  2.6, 2.6,  2.6, 2.6,  2.7,  2.7, 2.7,  3.0, 3.0, -1.0, -1.0,-1.0),
    cutvalmin = cms.vdouble( -1.0, -1.0, 1.0,  0.0, 0.0, -1.0, -1.0, 0.0, 0.02, 2.0, -1.0, 0.02,10.0),
    cutvalmax = cms.vdouble( 0.90, 0.90,-1.0, -1.0,-1.0, 0.90, 0.99,-1.0, 0.99,-1.0, 0.90, -1.0,-1.0),
)
