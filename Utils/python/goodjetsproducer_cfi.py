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

#Updated the values following: https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVUL 
    varnames  = cms.vstring('nhf','nef','nc', 'mf', 'chf', 'cm', 'cef','nhf','nef','nhf','nef','nm','nhf','nef','nm'),
    etamin    = cms.vdouble( -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,  2.4,  2.4,  2.7,  2.7,  2.7, 3.0,  3.0,  3.0),
    etamax    = cms.vdouble(  2.4,  2.4,  2.4,  2.4,  2.4,  2.4,  2.4,  2.7,  2.7,  3.0,  3.0,  3.0, 5.0,  5.0,  5.0),
    cutvalmin = cms.vdouble( -1.0, -1.0,  1.0, -1.0,  0.0,  0.0, -1.0, -1.0, -1.0, -1.0,  0.0,  1.0, 0.2, -1.0,  10 ),
    cutvalmax = cms.vdouble( 0.90,  0.90, -1.0, 0.80, -1.0, -1.0,  0.8, 0.90, 0.99, 0.90, 0.99,-1.0,-1.0,  0.9, -1.0 ),

    jetPtFilter = cms.double(30.),
    invertJetPtFilter = cms.bool(False),
    SaveAllJetsId = cms.bool(False),
    SaveAllJetsPt = cms.bool(False),
    ExcludeLepIsoTrackPhotons = cms.bool(False),
    JetConeSize = cms.double(0.04),
    SkipTag = cms.VInputTag(),
    puppi = cms.bool(False),
    puppiPrefix = cms.string(""),
)

from TreeMaker.TreeMaker.TMEras import TMeras
TMeras.TM2017.toModify(GoodJetsProducer,
    varnames  = cms.vstring('nhf','nef','nc', 'mf','chf','cm','cef','nhf','nef','mf','cm','cef','nef','nm','nhf','nef','nm'),
    etamin    = cms.vdouble( -1.0, -1.0,-1.0,-1.0, -1.0,-1.0, -1.0,  2.6,  2.6,  2.6, 2.6, 2.6.  2.7,  2.7, 3.0,  3.0,  3.0),
    etamax    = cms.vdouble(  2.6,  2.6, 2.6, 2.6,  2.6, 2.6,  2.6,  2.7,  2.7,  2.7, 2.7, 2.7,  3.0,  3.0, 5.0,  5.0,  5.0),
    cutvalmin = cms.vdouble( -1.0, -1.0, 1.0,-1.0,  0.0, 0.0, -1.0, -1.0, -1.0, -1.0, 0.0,-1.0,  0.01, 1.0, 0.2, -1.0,  10  ),
    cutvalmax = cms.vdouble( 0.90, 0.90,-1.0, 0.80,-1.0,-1.0,  0.80, 0.90, 0.99, 0.80,-1.0,0.80, 0.99,-1.0,-1.0,  0.9, -1.0),
)
# 2017 and 2018 has the same values.
TMeras.TM2018.toModify(GoodJetsProducer,
    varnames  = cms.vstring('nhf','nef','nc', 'mf','chf','cm','cef','nhf','nef','mf','cm','cef','nef','nm','nhf','nef','nm'),
    etamin    = cms.vdouble( -1.0, -1.0,-1.0,-1.0, -1.0,-1.0, -1.0,  2.6,  2.6,  2.6, 2.6, 2.6.  2.7,  2.7, 3.0,  3.0,  3.0),
    etamax    = cms.vdouble(  2.6,  2.6, 2.6, 2.6,  2.6, 2.6,  2.6,  2.7,  2.7,  2.7, 2.7, 2.7,  3.0,  3.0, 5.0,  5.0,  5.0),
    cutvalmin = cms.vdouble( -1.0, -1.0, 1.0,-1.0,  0.0, 0.0, -1.0, -1.0, -1.0, -1.0, 0.0,-1.0,  0.01, 1.0, 0.2, -1.0,  10  ),
    cutvalmax = cms.vdouble( 0.90, 0.90,-1.0, 0.80,-1.0,-1.0,  0.80, 0.90, 0.99, 0.80,-1.0,0.80, 0.99,-1.0,-1.0,  0.9, -1.0),
)

# separate version for puppi
GoodJetsPuppiProducer = GoodJetsProducer.clone(
    puppi = cms.bool(True),
    puppiPrefix = cms.string("puppiSpecificAK8"),
    varnames  = cms.vstring('nhf','nef','nc', 'mf', 'chf', 'cm', 'cef','nhf','nef','nm','nef','nm'),
    etamin    = cms.vdouble( -1.0, -1.0, -1.0,-1.0, -1.0, -1.0, -1.0,  2.4,  2.4,  2.7, 3.0,  3.0),
    etamax    = cms.vdouble(  2.4,  2.4,  2.4, 2.4,  2.4,  2.4,  2.4,  2.7,  2.7,  3.0, 5.0,  5.0),
    cutvalmin = cms.vdouble( -1.0, -1.0,  1.0,-1.0,  0.0,  0.0, -1.0, -1.0, -1.0,  1.0,-1.0,  2 ),
    cutvalmax = cms.vdouble( 0.90,  0.90,-1.0, 0.80,-1.0, -1.0,  0.8, 0.98, 0.99, -1.0, 0.9, -1.0 ),
)

TMeras.TM2017.toModify(GoodJetsPuppiProducer,
    varnames  = cms.vstring('nhf','nef','nc', 'mf','chf','cm','cef','nhf','nef','mf','cef','nhf', 'nef','nm'),
    etamin    = cms.vdouble( -1.0, -1.0,-1.0,-1.0, -1.0,-1.0, -1.0,  2.6,  2.6,  2.6,  2.6.  2.7,  3.0,  3.0),
    etamax    = cms.vdouble(  2.6,  2.6, 2.6, 2.6,  2.6, 2.6,  2.6,  2.7,  2.7,  2.7, 2.7,  3.0,   5.0,  5.0),
    cutvalmin = cms.vdouble( -1.0, -1.0, 1.0,-1.0,  0.0, 0.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0,  -1.0,  2  ),
    cutvalmax = cms.vdouble( 0.90, 0.90,-1.0, 0.80,-1.0,-1.0,  0.80, 0.90, 0.99, 0.80,0.80, 0.9999,0.9, -1.0),
)
# 2018 puppi-specific settings not available yet
TMeras.TM2018.toModify(GoodJetsPuppiProducer,
    varnames  = cms.vstring('nhf','nef','nc', 'mf','chf','cm','cef','nhf','nef','mf','cef','nhf', 'nef','nm'),
    etamin    = cms.vdouble( -1.0, -1.0,-1.0,-1.0, -1.0,-1.0, -1.0,  2.6,  2.6,  2.6,  2.6.  2.7,  3.0,  3.0),
    etamax    = cms.vdouble(  2.6,  2.6, 2.6, 2.6,  2.6, 2.6,  2.6,  2.7,  2.7,  2.7, 2.7,  3.0,   5.0,  5.0),
    cutvalmin = cms.vdouble( -1.0, -1.0, 1.0,-1.0,  0.0, 0.0, -1.0, -1.0, -1.0, -1.0, 1.0, -1.0,  -1.0,  2  ),
    cutvalmax = cms.vdouble( 0.90, 0.90,-1.0, 0.80,-1.0,-1.0,  0.80, 0.90, 0.99, 0.80,0.80, 0.9999,0.9, -1.0),
)
