import FWCore.ParameterSet.Config as cms

SelectPFCandidates = cms.EDProducer('SelectPFCandidates',
PackedPFCandidatesTag               = cms.InputTag('packedPFCandidates'),
MinPt								  = cms.double(5),
MaxEta								  = cms.double(5.0),
SelectpdgIDTyp							  = cms.int32(0), # 0 this is not used all others will be absolut values only! so only possitive values valid
)
