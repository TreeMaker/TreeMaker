import FWCore.ParameterSet.Config as cms

ZProducer = cms.EDProducer('ZProducer',
   ElectronTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
   MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon')
)

