import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/3F209CCC-C10A-2049-8AE4-C1371A26EF69.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/70831503-C4E4-4C49-BB3A-339A3957C4D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/72187F3B-4FAB-F94C-9597-051A7E8986DE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/80BF7A24-1FEC-FC41-9A6D-43E88A834464.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/B0D7BF3F-4E0A-1F4E-9215-4806D0341446.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/FAA17EF5-1291-AF49-A484-DB92DEF6BEB5.root',
] )
