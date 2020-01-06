import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5CD2EB74-020A-EA11-AEBB-FA163E02F296.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9ABDA84D-7DEE-E911-8112-FA163E19B27F.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FEC339CA-020A-EA11-9242-0CC47A78A360.root',
] )
