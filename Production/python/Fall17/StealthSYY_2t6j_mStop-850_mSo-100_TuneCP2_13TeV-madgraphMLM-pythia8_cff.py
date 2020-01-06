import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/0017D22B-39EE-E911-939F-FA163ED66871.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/42E788B1-5C03-EA11-9773-E0071B6CAD10.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4EB26080-5C03-EA11-BFC1-002481CFE1EC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/52D35769-5C03-EA11-869A-B02628341890.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/980CACD1-5C03-EA11-8180-FA163EE1A1B2.root',
] )
