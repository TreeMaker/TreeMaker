import FWCore.ParameterSet.Config as cms

leptontagandprobeproducer = cms.EDProducer('LeptonTagAndProbeProducer',
TagPFCand = cms.InputTag('LeptonsNew:IdIsoMuon'),
ProbePFCand = cms.InputTag('LeptonsNew:IdMuon'),
ProbeTestPFCand = cms.InputTag('LeptonsNew:IdIsoMuon'),
)
