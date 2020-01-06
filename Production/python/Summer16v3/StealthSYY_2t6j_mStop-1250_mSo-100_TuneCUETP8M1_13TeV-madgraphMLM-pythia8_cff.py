import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/00E6E13E-6CF6-E911-9FD9-002590DE6DE4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/060717C4-6CF6-E911-90F2-001E675A6D10.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/1C9A804D-6CF6-E911-8219-0CC47A7C3444.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/329145A6-6EF6-E911-B5D5-0090FAA58564.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3A036468-6EF6-E911-AB06-7CD30AD094B4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4A485B28-6CF6-E911-95D1-0CC47AFF249A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7A01243F-6CF6-E911-98B6-FA163E007F01.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7E611553-6CF6-E911-86AE-0025B3E025B6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/BE5F8937-6CF6-E911-8564-008CFAFBDC0E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C2DE9DF5-6BF6-E911-871F-44A842B4D8CB.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F2C051CF-6CF6-E911-A31D-002590EFF972.root',
] )
