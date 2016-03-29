import FWCore.ParameterSet.Config as cms

deltaphiqcd  = cms.EDProducer ( 'DeltaPhiQCD',
#    JetTagRecoJets      = cms.VInputTag ( 'MHTJets','HTJets' ) ,
#    JetTagGenJets       = cms.VInputTag ( 'GenMHTJets', 'GenHTJets' ) ,
#    BTagInputTag = cms.InputTag ( 'combinedInclusiveSecondaryVertexV2BJetTags' ) ,
    GenParticleTag = cms.InputTag ( 'prunedGenParticles' )
)

