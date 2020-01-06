import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/0A0E33D4-5CAE-C147-AB73-B6872E03D5A2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/43F12D4C-8283-6A41-9BFE-A7A624040635.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/8229866A-5F3B-F542-8946-F9DE325AA00C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/852A8FFA-40B2-0544-A7A3-02D4F7F4292A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/890CA18A-013F-E74B-87C8-4AF0CCD6FD89.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/CD2EAF36-8026-F14B-8D8F-BC2FFED9E971.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/DA39E88B-1D26-7540-8AD4-5DB50D3F50AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/E04C4181-EB42-7743-BA99-3A51888D3C06.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/E4FB70B7-A43F-594A-B06A-891AC33F2DF6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/EE5286E9-7FE4-4144-89E9-EFA4C880000B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/FB6F241D-8B1A-CE47-BDAC-CCF15F4F05BC.root',
] )
