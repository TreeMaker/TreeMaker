import FWCore.ParameterSet.Config as cms

TruthNoiseFilter = cms.EDFilter('TruthNoiseFilter',
                                genjetCollection = cms.InputTag('slimmedGenJets'),
                                jetCollection = cms.InputTag('slimmedJets'),
                                recoJetPt = cms.double(100.),
                                genJetPt = cms.double(20.),
                                dRmax = cms.double(0.05)
                                )
