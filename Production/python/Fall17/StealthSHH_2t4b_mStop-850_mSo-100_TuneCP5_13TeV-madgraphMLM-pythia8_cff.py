import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/3444CBC7-9FAB-E811-BFB6-0CC47A78A41C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/AAF633DC-D3A9-E811-9565-90B11C443C9E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/B612E849-9CAB-E811-A865-FA163EC5C758.root',
] )
