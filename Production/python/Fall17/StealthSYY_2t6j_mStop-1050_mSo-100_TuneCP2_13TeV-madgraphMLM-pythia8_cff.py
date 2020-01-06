import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/14D83220-7CFE-E911-9E0E-44A842CFC97E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/28F85018-73FE-E911-9361-7CD30AC03054.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6A5B289B-FAFE-E911-BA55-FA163E544C3B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6ABE9DCF-34FE-E911-9050-1CB72C1B64E6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/880F1D0A-4CFF-E911-8329-0090FAA57310.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/9A772092-29FE-E911-BBDD-7CD30ACE1660.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B0276955-34FE-E911-879C-44A842B4D8D8.root',
] )
