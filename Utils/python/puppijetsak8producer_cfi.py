import FWCore.ParameterSet.Config as cms

PuppiJetsAK8Producer = cms.EDProducer('PuppiJetsAK8Producer',
                                      JetTag = cms.InputTag("slimmedJetsAK8"),
                                      SubJetTag = cms.InputTag("slimmedJetsAK8PFPuppiSoftDropPacked"),
                                      debug = cms.bool(False)
                                      )
