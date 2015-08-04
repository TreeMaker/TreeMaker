import FWCore.ParameterSet.Config as cms

GoodJetsProducer = cms.EDFilter('GoodJetsProducer',
				 TagMode = cms.bool(False),
                 JetTag = cms.InputTag('slimmedJets'),
                 maxJetEta = cms.double(5.0),
                 maxMuFraction = cms.double(2),
                 minNConstituents = cms.double(2),
                 maxNeutralFraction = cms.double(0.99),
                 maxPhotonFraction = cms.double(0.99),
                 minChargedMultiplicity = cms.double(0),
                 minChargedFraction = cms.double(0),
                 maxChargedEMFraction = cms.double(0.99),
                 jetPtFilter = cms.double(30.),
                 ExcludeLepIsoTrackPhotons = cms.bool(False),
                 JetConeSize = cms.double(0.04),
                 MuonTag = cms.InputTag('LeptonsNew:IdIsoMuon'),
                 ElecTag = cms.InputTag('LeptonsNew:IdIsoElectron'),
                 IsoTrackTag = cms.InputTag('IsolatedTracks'),
                 VetoHF = cms.bool(False),
                 VetoEta = cms.double(3.0)
)
