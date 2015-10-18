import FWCore.ParameterSet.Config as cms

JetsForHadTauProducer = cms.EDProducer('JetsForHadTauProducer',
JetTag = cms.InputTag('slimmedJets'),
reclusJetTag = cms.InputTag('patJetsAK4PFCHS'),
jetPtCut_miniAOD=cms.double(10),
genMatch_dR=cms.double(1),
dR_for_xCheck=cms.double(0.2),
relPt_for_xCheck=cms.double(1e-2),
useReclusteredJets=cms.bool(True),
MCflag=cms.bool(False),
debug=cms.bool(False),
)
