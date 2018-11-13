import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/06EF0D4E-9098-E811-9F66-A0369FE2C14A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1ACFDEAA-9198-E811-A03D-A4BF01033716.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1C1E8EA5-9198-E811-8228-008CFA165F58.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/260B14BA-9198-E811-81E2-0CC47AD98BEE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/548980A1-9198-E811-AF9E-801844DEED78.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/68781B32-9098-E811-B2CF-FA163E157838.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/98C3C74B-9098-E811-A8E4-141877642FAD.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B42522D0-9298-E811-96B8-AC1F6B0F3506.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/FED6095D-9198-E811-AF8E-EC0D9A8222CE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/088E4323-59A1-E811-AEEC-00259075D72E.root',
] )
