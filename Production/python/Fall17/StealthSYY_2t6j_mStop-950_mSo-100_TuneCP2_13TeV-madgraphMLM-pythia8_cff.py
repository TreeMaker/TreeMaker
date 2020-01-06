import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/08D82AA6-FB02-EA11-A2EE-AC1F6B23C88C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/4A889D2C-A7F8-E911-8B3E-0CC47AB64FB2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/6A5D9388-ACF7-E911-8675-AC1F6B23C77C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/9E8D5379-FA02-EA11-ACDA-B496910A8A88.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/A6AC4357-FB02-EA11-83BD-0242AC130002.root',
] )
