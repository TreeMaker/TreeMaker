import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/406009D1-E9B7-E611-A15C-D067E5F91A58.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/50A2398C-06B8-E611-AF31-D067E5F91B8A.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5231C73A-CBB7-E611-AB43-001E674440E2.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7EDB069C-0DB8-E611-98F4-0242AC130008.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8AABD071-CEB7-E611-8B10-001E67346BA1.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9CA87C05-B2B7-E611-9D97-001E67444EAC.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A889D87A-C6B7-E611-93AE-001E67397CB5.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BC527183-C0B7-E611-BC15-001E67348055.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C297C770-EBB7-E611-AD52-008CFA197C70.root',
       '/store/mc/RunIISummer16MiniAODv2/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C2A8E7F6-0BB8-E611-AD0C-0242AC130002.root',
] )
