import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/6CD61A55-86F0-E811-A3B4-002590147C5A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A66541BA-9AF0-E811-BE4A-1866DA890B94.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/D0982F03-93F0-E811-9D25-842B2B7680DF.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/EED5172E-84F0-E811-A0F6-1866DA8908C7.root',
] )
