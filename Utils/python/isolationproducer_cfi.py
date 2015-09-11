import FWCore.ParameterSet.Config as cms

isolationproducer = cms.EDProducer('IsolationProducer',
                                   LeptonTag = cms.InputTag('LeptonTag'), # these are the leptons that pass ID
                                   LeptonType = cms.string('LeptonType'),
                                   PFCandTag = cms.InputTag('PFCandTag'),
                                   JetTag = cms.InputTag("JetTag")
                                   )
