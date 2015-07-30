import FWCore.ParameterSet.Config as cms

JetCleaner = cms.EDProducer('JetCleaner',
   JetTag  = cms.InputTag('GoodJets'),
   ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
   ElectronR = cms.double(0.4),
   MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon'),
   MuonR = cms.double(0.4),
   PhotonTag = cms.InputTag('GoodPhotons:BesPhoton'),
   PhotonR = cms.double(0.4)
)

