import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1902BF48-80A8-2A40-94DE-DC069A98E41C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/30AD513C-D914-6140-8779-CB84C8F30497.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3DCCEC9B-2B5F-5C44-BF88-051CAFB05B7A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/56159080-F2D1-C049-96D3-1E6C9155DB16.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/6A791D4B-53F0-D147-B802-EFBEDC6239E2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8BCC3578-6683-D443-ABBF-3E4B656F0819.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9259E655-6FF6-3D41-9A90-F02069FBADAF.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A8345F42-F552-2347-BB39-D8BD1BB5F35C.root',
] )
