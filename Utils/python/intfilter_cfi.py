import FWCore.ParameterSet.Config as cms

IntFilter = cms.EDFilter(
'IntFilter',
IntTag          = cms.InputTag('IntTag'),
CutValue	= cms.double('1'),
CutType	= cms.double('1'), # defined 0 : var>cut , 1: var<cut , 2: var>=cut, 3: var<=cut; so 0 means if var>cut no cut applied
)
