import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/06D3EFF5-AAD2-2445-A159-06C3A73321C4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/0A84C16E-14EE-2941-9725-E0079D41A9CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/1275F0C2-2D12-B943-AB78-5BB3366CE9EE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/2380BB96-5B9D-CB46-9174-AADCC6714DAE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/4EA45691-B89C-F444-9890-FBD8643F4D29.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/5EE7E628-ED19-E34B-A81D-51191E1D8BC3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/5EE9ADDC-D0C1-B143-B920-6273D09BB00F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/61C32DD4-1734-6942-9681-FB1F67AE6476.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/663BEECE-79B8-2543-AE19-D65B0B44079B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/67CBF38F-7A1E-7F46-ADAB-1B3FD7A211D5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/8AEEF569-7104-F245-A5FC-987FB2C12D77.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/8D9296A7-9775-5446-BB28-9D5BD0879C16.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/989C7AE3-94F4-4243-B0BC-4C1575FF1608.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/9A79C5CE-CCE1-1344-B1D9-29E36CD079F1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/A29E7C21-EC09-F541-BBCA-E8A89BDA4975.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/B06CCD11-D124-EF44-B6D8-9876F3FC25D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/B59CE3F6-1ACE-044F-BF22-2C4846F72F97.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/C201CD5E-A5FD-F348-B12B-9D137430B62B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/DF0079F1-F274-CB41-A289-58F4401D0460.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/E6E6B507-023F-4847-84C2-A9C3E2DEBE80.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/40000/EE4D6184-2C62-5443-AEC5-E1686A20B707.root',
] )
