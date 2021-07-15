import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/03EFF4E3-1F65-1949-8DBF-4F05591F4D07.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/083B2946-AA40-8140-88B5-8DB5B01DC8E4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/0A3FAAF3-CE54-EA4C-9407-282E8E032DA4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/0B75A3C7-8FC9-E04F-99DE-5DC23961C7B1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/0FD23FCF-ACD7-344D-BE33-97AA7E47A252.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/1F1ECFBB-445F-644B-8FA7-4121386596C2.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/29061AEE-4EFE-C54C-BCBA-F8D188F8CFCF.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/2AC8FCFE-5A66-2046-A23B-F65FE1852AA9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/2EDF49E6-07DC-B947-8D1E-23814F32D731.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3038B180-47FA-384B-9FD2-7EF3E76FA4F5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/356BA4FF-FFBB-F442-A029-D8E5E097350F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3F2919F1-BAC4-EB4C-942C-F673CD603144.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/65548418-D915-BA4A-86CA-8D5ED90C36CB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/65712AEF-261D-C845-9DCD-D95EE7DA68E9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/6A0C68E8-2506-2740-81C6-59E4F9D1A0C8.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/6DD24AF7-CD84-634B-968A-4E0F581D38F7.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/6E2A962E-85E6-5F4D-8548-2F96A92E2E49.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/703DE884-1B0A-DE44-AAC1-6C1A80F488BE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/7485F9FC-1D3C-344F-BE4D-63886A8D474A.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/7FA10B0B-377F-2746-8F9B-E46D78C0191D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/8BB84E6D-C416-DB46-BD4D-22A71D399CD6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/8C004F4B-2515-CA46-A2A1-082F43085462.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/8D746684-D037-2A46-BFB4-BA68F1251792.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/A349F0D1-569B-154B-BC30-0999A6F606BD.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/C2289D8A-DCDD-244C-A2BF-C53A41D81521.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/CD368B52-4161-EB45-9B10-ADDED7F2F6C8.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/DD0839C7-0A72-BD42-B062-0EE6779BAF22.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/DD40E111-CDC5-D248-B366-563D569D29B1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/E07E8A64-4C7E-D147-A70A-338BCC466909.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/E3086BB2-34C5-EF43-B7CE-6A212E6E588F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/E706B29E-E797-654B-8848-7F6FE5311AB7.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/EC2BF272-DAE6-544F-9C80-0EC016EC01BE.root',
] )
