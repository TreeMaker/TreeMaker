import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/04165721-C4F0-E811-A838-0025905B8590.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/46AA75BA-B8F0-E811-8C4A-0CC47A4D7616.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/74A8E752-B4F0-E811-A943-0CC47A78A30E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B0E5BB89-D0F0-E811-B3B3-0CC47A4D764C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C40B58B8-BCF0-E811-9079-0CC47A7C3404.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/CA489959-ABF0-E811-83C6-0025905B855A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/927F7F33-BAF0-E811-8491-0CC47A7C35C8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/A490A70F-5BF1-E811-BD7F-AC1F6B0DE0C4.root',
] )
