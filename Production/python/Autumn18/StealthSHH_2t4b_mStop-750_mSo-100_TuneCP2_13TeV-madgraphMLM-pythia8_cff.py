import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/07DE9FFB-B3CE-DC4A-9E75-46A39D231996.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/0C4B2486-C234-5C4B-8A09-E1F37A7AC6D4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/1AFDB4C8-A3BA-2F4C-8053-D2EC77055E84.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/294A861E-6426-3048-B368-46DFDAEBD0A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/3BD38A87-2C93-EA49-AECE-47F4CA377A2C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/41BC9D7E-FB89-4646-8BA8-C9018D78F4FB.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/41C1AF08-A996-594D-A4BF-582A2967539F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/49C88D99-269B-0049-847B-E2CFF0C7BC84.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/54F3E107-623C-EE42-85DD-1177656B4691.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/7C896501-2996-8849-AC95-F421DD93EFA2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/8C215C13-711B-3D41-878C-9D5EF39871D9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/9D1E691D-9A41-1740-9226-1D407B6DB82D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/B753F14F-6879-044C-9F3D-7D361F56750F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/CC1842A7-ADDE-5F41-8460-4F34A9568BE8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/E0E3D11E-70DE-8E4D-93BD-E55D84986F30.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/FC8F6233-5F6F-284C-9140-0D3E9C631E78.root',
] )
