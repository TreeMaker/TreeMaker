import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/010000/94166749-D818-E911-9EBE-AC1F6BAC816C.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/010000/AECB6E5D-E818-E911-9787-0CC47A7C3444.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/10000/C452A24B-5218-E911-9917-AC1F6B8AC010.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/40000/0E99025F-CB1D-E911-BF40-0CC47A7C3412.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/40000/561B941C-AD1D-E911-BD60-AC1F6B8AC3A2.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/40000/C4E52AAD-9D1D-E911-8062-0CC47A78A360.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/40000/D41C095F-CB1D-E911-9656-0CC47A7C3412.root',
] )
