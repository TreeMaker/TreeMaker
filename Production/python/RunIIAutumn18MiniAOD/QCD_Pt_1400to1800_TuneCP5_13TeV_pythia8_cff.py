import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/46630CF5-C38A-4F4E-AA33-993F368B545A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/46C73C7B-24AC-2E44-9B5B-3D272BD9A833.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/50EA1C02-E1E0-9042-8595-28A606AAB941.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/56129E5A-31FD-A842-9532-C9498CA164B1.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/7406252D-A92E-E54B-A585-4490782A3B84.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/A3FC647A-024C-A443-9D18-D913B7BDAC88.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/AF144461-4AED-0B4B-A8A1-F3691E221A91.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/BA4B2CE9-6A37-3948-9880-E9927286DE6B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/BB057698-1A58-FB48-882E-88D42E9C1407.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/C18C4710-6C8B-644F-814B-D4D920E48EC9.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/CDFCA729-AC4E-D547-B8D4-4B8A4B24A793.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/110000/E8D0D83E-180F-7240-A08F-99D228FADB75.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/0B07ADC5-0FFD-3448-BB79-FC33CB1B0255.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/0FEC4D57-E5E5-364A-8231-9207B7BBE189.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/154BF447-95FD-C84E-BC7D-6C837FB9A783.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/1CDAC357-29F8-6648-8293-CEBC71C78F63.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/2426277A-AF0A-914F-ACB3-969C0D32C3F6.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/2DBA1A21-1BA6-8D47-A973-CE6B3F270963.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/40E1F089-71DE-624D-8E1B-B4B0D9608563.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/625B2585-194F-9A49-BAAE-1423D0B7A1F1.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/77A75B76-FE2F-F64B-BC65-9D5CC92A019C.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/91D6C74B-1673-5B47-9373-EB2A507B65C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/92197B42-17FC-DF47-992D-6836BAE7CF7F.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/A3672F48-093B-4140-A259-FD823FB85F37.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/BEACC848-9E30-BE4D-AF18-ADC9486A2AC9.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/D192D39C-338C-154F-9AB3-7A27D29ACA1E.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/E219A9B7-73FC-4348-AEF1-36AD15898DA8.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/E8380042-2D2C-5A4D-A4BF-98C42B2D02D8.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_102X_upgrade2018_realistic_v15-v1/120000/E9909940-D481-8843-A9DC-E408F7328B6C.root',
] )
