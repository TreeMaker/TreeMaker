
import FWCore.ParameterSet.Config as cms

activityProducer = cms.EDProducer('ActivityProducer',
objectSource   = cms.InputTag('probeMuons'), # probe source eg (IDmuons)
objectMatchSource   = cms.InputTag('objectMatchSource'), # to be matched to collection  (IDIsoMuons)
objectTyp = cms.int32(0), # 1 muon 11 muon with starting from probe track, 2 electron 22 electron starting from photon as probe
activityTyp = cms.int32(0),
maxDeltaR = cms.double(1.0),
jetSrc = cms.InputTag('slimmedJets'),
TagObjectForMTWComputation = cms.InputTag(''),
METTag = cms.InputTag('slimmedMETs'), 
)