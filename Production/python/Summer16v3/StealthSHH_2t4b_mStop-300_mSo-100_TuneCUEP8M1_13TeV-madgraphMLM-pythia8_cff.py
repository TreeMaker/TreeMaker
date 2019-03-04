import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/20779905-E0EF-E811-8DE6-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/903AF9B3-0DEF-E811-9165-0242AC1C0507.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/74EA3243-0CF3-E811-8A88-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/7697CEA2-75F3-E811-AB71-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/210000/F8F1C253-0DF3-E811-8E24-0242AC1C0502.root',
] )
