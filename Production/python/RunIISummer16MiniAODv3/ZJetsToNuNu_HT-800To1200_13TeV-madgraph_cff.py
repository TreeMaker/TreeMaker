import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0817ABD3-7209-E911-A856-0242AC1C0504.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/CAC455FA-6809-E911-98E4-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/1AD19338-1606-E911-BA9B-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/2613ADD6-1506-E911-B2FD-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/2A945D16-1406-E911-846C-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/34F1CDDD-1506-E911-9CB9-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/3E1430C6-1106-E911-AAD1-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/403282F5-2406-E911-B8F0-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/44B3D92A-1806-E911-9DE4-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/5A20F634-1406-E911-A112-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/622F89DE-1506-E911-B5DD-0242AC1C0506.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/62E4D809-1306-E911-9537-0242AC1C0505.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/8E206102-1606-E911-A0E6-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/9E4CF157-1C06-E911-B62F-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/9EBF6CCD-1206-E911-80CE-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/CA3FB3EE-3A06-E911-8FDA-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/DA33270A-1606-E911-9B6C-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-800To1200_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/EC8B0D23-1B06-E911-A7AC-0242AC1C0500.root',
] )
