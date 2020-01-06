import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0285FEBE-7418-5248-B2BE-219ED89335EE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/074BD4B7-E453-F84F-903D-671C28804BA2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1BE58F21-FA2F-F141-A538-05387AA31699.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4B002876-757E-AC49-BF0A-46819833CEA8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/62D44AB0-50DC-C64D-82CF-66AC52948632.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/75E8EA86-0FD9-FC4B-B06E-C796AD0C2E3F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/77575E23-738B-E248-B06B-7C18B8DDF78D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/81F3AF5C-843B-1C40-92DC-F698811C8409.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8A6950FB-9D86-CF4B-9E25-646E62ECD185.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8D42A16A-CAF2-0D42-9A82-B6EFCE71AA87.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AC83C5A0-3D66-2243-9826-8EE69545D0F0.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C0E2F31F-6A37-814F-9EAF-4C70C646C10D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/FF6F15FA-981C-D849-9C41-14F2B553314B.root',
] )
