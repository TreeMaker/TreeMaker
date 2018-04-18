import FWCore.ParameterSet.Config as cms

isolationproducer = cms.EDProducer('IsolationProducer',
                                   LeptonTag = cms.InputTag('LeptonTag'), # these are the leptons that pass ID
                                   LeptonType = cms.string('LeptonType'),
                                   PFCandTag = cms.InputTag('packedPFCandidates'),
                                   JetTag = cms.InputTag("HTJets"),
                                   RhoTag = cms.InputTag("fixedGridRhoFastjetAll"),
                                   electronEAValues = cms.vdouble(0.1752, 0.1862, 0.1411, 0.1534, 0.1903, 0.2243, 0.2687),
                                   muonEAValues = cms.vdouble(0.0735, 0.0619, 0.0465, 0.0433, 0.0577)
                                   )
