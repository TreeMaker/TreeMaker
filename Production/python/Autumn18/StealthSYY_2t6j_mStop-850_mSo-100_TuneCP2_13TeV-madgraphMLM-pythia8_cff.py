import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0C1ED71D-90BF-B14A-AE08-E23268F2AD80.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1A245365-09A1-1A45-98CF-9B15FD9DDBDF.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/2FC3E2D0-E356-CB43-95BD-84C0E44325A2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/419AAC8D-3C4A-B04E-92E6-47A2A59C1057.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/527633F4-4993-1847-B21F-6397E1F0E5AD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A1624F6C-371D-5547-B2E2-36E7BEEF0863.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A1C52BB1-69DA-B24A-8F6A-4A849B89CF98.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C81FB1FB-BBC9-9F4E-B123-8B18851E965F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D29FB516-712B-0147-A9B2-AF5CE675E98B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E655293A-6E42-964F-B720-42CAFA3E0B0C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F2FA80CA-CB67-024D-98D4-39D29C9FA6A7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F5ED4EE5-7DCE-5F49-93DA-396ABB6C444F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F67C747E-1978-7641-B0EE-8FCE6F8FF227.root',
] )
