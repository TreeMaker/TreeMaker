import FWCore.ParameterSet.Config as cms

MCResolutions = cms.EDAnalyzer('MCResolutions',
   leptonTag         = cms.InputTag('GoodLeptons'),
	jetTag				= cms.InputTag('GoodJets'),
   btagTag           = cms.string('combinedInclusiveSecondaryVertexV2BJetTags'),
   btagCut           = cms.double(0.814),
	genJetTag			= cms.InputTag('slimmedGenJets'),
	weightName			= cms.InputTag('WeightProducer','weight','ResponseTemplates'),
	jetMultPtCut      = cms.double(30.),
	jetMultEtaCut     = cms.double(2.4),
	deltaPhiDiJet		= cms.double(2.7),
	absCut3rdJet		= cms.double(30.),
	relCut3rdJet		= cms.double(0.2),
	deltaRMatch			= cms.double(0.25),
	deltaRMatchVeto	= cms.double(0.7),
	absPtVeto			= cms.double(20.),
	relPtVeto			= cms.double(0.01),
	GenJetPtCut			= cms.double(0.),
   fileName				= cms.string('MCJetResolution.root')
)
