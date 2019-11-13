import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/030AAAB6-A84C-8248-AAC8-68FDA01D116F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/1377BC65-E1D0-5242-95A3-93382CAC6DB1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/17E84B2E-71FB-674D-BF6E-BC02B93489BD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/255AEA1E-3631-FC40-979E-E0A1BD59D133.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/28B82D5C-0F19-1445-B11E-1409F59F1051.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/2EB38D79-47E6-5D44-A3D6-B4A22347A97C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/36B3C02B-7556-374E-9164-C4FF148DC1B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/544CE7A5-5F4B-CA4F-BFF5-46FA319B91C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/548956DA-C15F-9C45-B6BD-B2E059D129E8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/6F332DAA-D535-D540-A5A9-27F8CB80EAA2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/7A09AE38-5695-0140-BD53-D6A693A0F765.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/9B77BBD9-F24D-C64A-A241-F0171AC590B5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/A3B31203-FE4E-CA42-A5E5-9C0E6E43856C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/B56C1DAC-13ED-E94B-A10D-B6FAC577F487.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/BC668C23-3BBC-C041-BEA6-4B583A406391.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/E18B5C20-D166-694B-956F-F2F985813C74.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/E3F4445E-EA58-4D41-822C-2242F231B8E7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/EC8F82D3-C919-C840-948D-497C946805BA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/F1ABFCA1-3623-6F4E-B96D-02C4D45B21FE.root',
] )
