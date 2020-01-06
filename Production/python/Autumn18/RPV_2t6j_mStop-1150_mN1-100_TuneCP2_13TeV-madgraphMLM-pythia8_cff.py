import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1C3D7FC6-B0AC-174E-A43D-BF3FDABF7A4C.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/24C6ACD2-9F61-3E48-8FE4-160D2D832350.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/407B7C8B-96BF-594D-BDE4-E98432268BC3.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5181730D-6F0C-5B4F-84DA-14ED5AA4E6CA.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5D63F6F1-0F7B-E644-A319-46214E251F2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/ABC18345-1C5F-A348-8DFF-ED4FF68E1EE6.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CB61DF18-5AD8-8247-A58B-83EA6BB7FCB7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1150_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F7BE7143-20B3-7F49-9EB2-1D16E180EABC.root',
] )
