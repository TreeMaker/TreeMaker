import FWCore.ParameterSet.Config as cms

extrapolationproducer = cms.EDProducer('ExtrapolationProducer',
                                       MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon'),
                                       ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron')
                                       )
