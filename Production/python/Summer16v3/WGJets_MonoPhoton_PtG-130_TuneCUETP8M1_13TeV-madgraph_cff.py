import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/645EB628-7B16-E911-8803-E0071B7A3540.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/F831E475-2F16-E911-B02E-24BE05CE2EE1.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/067A9165-CD16-E911-9FDA-24BE05C44BB1.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/80A5F099-7B16-E911-A7F4-24BE05C616E1.root',
       '/store/mc/RunIISummer16MiniAODv3/WGJets_MonoPhoton_PtG-130_TuneCUETP8M1_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/F8F9FF35-7C16-E911-BB14-24BE05CEEC21.root',
] )
