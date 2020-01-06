import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8088F5AD-7FED-E911-B531-FA163EF0622C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B6973731-6A02-EA11-AC23-0025905B858C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/BED68CC9-1801-EA11-AA3A-FA163EB631D4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C2A5DF7E-8801-EA11-B32A-5065F3815241.root',
] )
