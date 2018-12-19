import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/2EBA4EF4-B3EF-E811-A152-20CF3027A568.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A047B256-BCEF-E811-AA8E-20CF300E9EB7.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A49C2D4F-E0EF-E811-9FBF-00259021A076.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/A4D7DB18-0FF0-E811-8E0D-901B0E6459CA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B23AF4FC-D3EF-E811-AEDC-20CF3027A5A3.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B28C4BDE-C6EF-E811-946D-003048FE2B6C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C6668F63-C4EF-E811-88F4-246E96D1486C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/D42EF144-C9EF-E811-B843-0CC47AFC3C9C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/E266342B-DCEF-E811-8448-20CF3019DF19.root',
] )
