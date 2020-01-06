import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-900_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/0C60B7BE-B5F4-E911-9D9C-AC1F6BABF8D5.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-900_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/74E419BD-36F4-E911-8E99-A4BF012835C2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-900_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/A4105585-44F5-E911-AB96-0090FAA57360.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-900_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/D06063CF-2FF4-E911-9C8C-AC162DB52EF0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-900_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/EEBA7059-3EF4-E911-9CB8-FA163E5451BE.root',
] )
