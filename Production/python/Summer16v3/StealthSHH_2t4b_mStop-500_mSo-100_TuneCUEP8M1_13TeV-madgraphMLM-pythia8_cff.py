import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/949F289F-2FEF-E811-A879-0CC47A7C347E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/BA02C4CB-88EF-E811-AA25-0CC47A745282.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-500_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/DC604659-3AEF-E811-82C1-0025905A6094.root',
] )
