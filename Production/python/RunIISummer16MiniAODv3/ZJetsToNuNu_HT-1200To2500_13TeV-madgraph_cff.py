import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/00C8CA7E-1B06-E911-889E-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/0ABDB134-1B06-E911-9728-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/68E753F5-9D06-E911-ADA6-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/280000/E2B5509A-1D06-E911-960B-0242AC1C0501.root',
] )
