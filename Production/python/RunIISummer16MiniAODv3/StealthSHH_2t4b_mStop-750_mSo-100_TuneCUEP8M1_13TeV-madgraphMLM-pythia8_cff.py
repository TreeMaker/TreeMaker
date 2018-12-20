import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/2CDE0427-2CEF-E811-B331-008CFA110AE8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/3679F246-29EF-E811-849D-008CFAC940D0.root',
] )
