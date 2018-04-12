import FWCore.ParameterSet.Config as cms

DoubleFilter = cms.EDFilter(
'DoubleFilter',
DoubleTag          = cms.InputTag('DoubleTag'),
CutValue	= cms.double(500),
)
