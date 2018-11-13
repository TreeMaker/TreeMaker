import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/2245B67E-A9AC-E811-A876-5065F38182E1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/4E60FFA7-A9AC-E811-BD80-0025901D08B0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/7ED9EC93-A9AC-E811-AB7A-842B2B6AE7CA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/C2ECF6B9-A9AC-E811-8226-3417EBE643DE.root',
] )
