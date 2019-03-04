import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/16D5849D-50F3-E811-89F4-0CC47AFC3C86.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/A20E29A7-50F3-E811-B87F-246E96D1486C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-550_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/90000/B00FBC7C-60F3-E811-A207-0CC47AFC3C98.root',
] )
