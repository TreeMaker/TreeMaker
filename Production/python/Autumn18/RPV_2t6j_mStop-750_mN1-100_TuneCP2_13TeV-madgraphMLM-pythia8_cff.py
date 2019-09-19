import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/007DFEB4-8C3B-6F41-A5B3-C38514E87746.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/13C57942-B960-4F48-ACD0-152BB0D1975C.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/203ACA86-FD86-5142-85FB-A125ACEC62F3.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/675A2E8A-74F3-AE49-B82A-4AB8F7BDDC61.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/72A18F67-0797-394A-9E57-0CFC3C0FBC2F.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/8A181522-F22B-F44A-AA86-CAB1CC4DC9FE.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/A75AA46C-7A3F-DA40-B89C-50DEA3A26B28.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/B7B67254-DF5D-F14F-A828-64228200428D.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/BA1C6888-680B-BB45-B343-E03719AA84A8.root',
] )
