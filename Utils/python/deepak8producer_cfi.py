import FWCore.ParameterSet.Config as cms

DeepAK8Producer = cms.EDProducer('DeepAK8Producer',
    JetTag = cms.InputTag("slimmedJetsAK8"),
    datapath = cms.string("NNKit/data/ak8/full"),
)

DeepAK8DecorrelProducer = DeepAK8Producer.clone(
    datapath = cms.string("NNKit/data/ak8/decorrelated"),
)
