import FWCore.ParameterSet.Config as cms

SubJetSelection = cms.EDProducer('SubJetSelection',
                                 JetTag = cms.InputTag('slimmedJets'),
                                 MinPt = cms.double(30),
                                 MaxEta = cms.double(5.0),
)

SubGenJetSelection = cms.EDProducer('SubGenJetSelection',
                                 JetTag = cms.InputTag('slimmedGenJets'),
                                 MinPt = cms.double(30),
                                 MaxEta = cms.double(5.0),
)