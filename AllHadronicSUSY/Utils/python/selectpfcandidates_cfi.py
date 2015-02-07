import FWCore.ParameterSet.Config as cms

SelectPFCandidates = cms.EDProducer('SelectPFCandidates',
PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
MinPt								  = cms.double(5),
MaxEta								  = cms.double(5.0),
)
