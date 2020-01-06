import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/000CD0CC-3DBB-B644-AF14-AEBD44712807.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/29682CAC-1D79-E244-8982-A95DE530E127.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/30367AA4-BDD7-5649-8D82-EAC74AD1B418.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/43FCF373-11C7-3647-8F2E-E4EA13081347.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/66947834-E28D-2D40-BC31-4396D68CE603.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/697C9942-AB62-6B4C-A3CF-AB141A3314F1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/845521CB-77C1-F840-9855-8FEF6417A096.root',
] )
