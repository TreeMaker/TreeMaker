import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/204C63D4-45EF-E811-BD6D-0CC47AF9B32A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/2C487648-5CEF-E811-8E52-0CC47AFCC40A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-650_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/9CAA65D2-B0EF-E811-8632-000AE488B7C8.root',
] )
