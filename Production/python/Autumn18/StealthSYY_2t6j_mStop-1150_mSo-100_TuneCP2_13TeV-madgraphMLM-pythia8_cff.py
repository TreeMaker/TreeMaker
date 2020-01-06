import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/01425D30-691F-E948-B0E1-EC944FE6DA84.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0FF7229C-A4D8-EE48-A4B3-234231E9784F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3AD23D68-EDBC-B94D-88CE-27B322BB9133.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/62FCB750-828D-2844-9A7D-21822D5E68B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/968E9CC4-E33E-4E41-8672-EA93A245CCDB.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/98168CAF-818D-8845-B24E-50840EDF7B71.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A12CE888-C08B-E94A-B0F1-E2E989B3A181.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AFDE8AA8-823C-8D4D-8838-0E72B01B4CE7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B34C56B3-86A6-C048-A64E-40B32B91B475.root',
] )
