import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/129514F3-C1A9-E811-A6D5-7CD30ACE2320.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/BC4209E4-9BAB-E811-A925-141877268DC6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/D80D7F43-9EAB-E811-B737-0025905B859E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/E4BAB0E6-C1A9-E811-B214-FA163E67E266.root',
] )
