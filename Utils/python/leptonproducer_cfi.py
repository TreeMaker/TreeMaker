import FWCore.ParameterSet.Config as cms

leptonproducer = cms.EDProducer('LeptonProducer',
MuonTag = cms.InputTag('slimmedMuons'),
ElectronTag = cms.InputTag('slimmedElectrons'),
PrimaryVertex = cms.InputTag('offlineSlimmedPrimaryVertices'),
minElecPt								  = cms.double(10),
maxElecEta								  = cms.double(2.5),
minMuPt								  = cms.double(10),
maxMuEta								  = cms.double(2.4),
muIsoValue								  = cms.double(0.2),
elecIsoValue								  = cms.double(0.2), # only has an effect with useMiniIsolation
UseMiniIsolation = cms.bool(False),
METTag = cms.InputTag('slimmedMETs'), 
rhoCollection = cms.InputTag("fixedGridRhoFastjetAll")
)
