import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/668D9AC9-1F01-EA11-8AD7-FA163E192CD3.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/6CDAEA78-5C03-EA11-A5C2-484D7E8DF0FA.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C27B402C-1801-EA11-BD1F-5065F3812261.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D60869E2-8801-EA11-82F7-40F2E9C89ED6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F4F9055D-3803-EA11-BE8A-AC1F6BAC7C1A.root',
] )
