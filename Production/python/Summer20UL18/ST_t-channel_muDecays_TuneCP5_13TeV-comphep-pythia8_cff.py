import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/0C44730E-6D8F-4641-B3FE-135554B9D78D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/1C7DD736-C4E6-A041-AF92-F28C812EC561.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/2136CC44-FA31-BC4B-AD2A-1E727EDCC275.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/33737176-D560-A048-AF0B-211D742A3810.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/37FAE5EE-D2CA-1848-A6B8-9B40DFB31CD6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3D4E74E7-9992-0743-B42F-B6E6615CB228.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/42AB460C-3FEF-654F-B20A-1C2554227CA9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/533064C7-0557-734B-AB56-638224779593.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/5430F1A4-14EF-5640-A4D0-0C05F8F75EA7.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/5C5A2E0B-3002-9947-AADF-7D15C45011EB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/614554DE-01C5-D748-ABCF-6CAB886CA6E8.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/6C20B211-DB31-6245-9BD2-B4878CD4FEEE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/6FC7BBEA-D0B1-D049-9FAD-7462A6DBCE5D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/7A286861-9AAE-0340-A9E4-A37827E78AEC.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/82035A90-B0D1-A048-8619-CB9130F53872.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/88469EFF-89B8-CD49-A849-E8C016F10BB3.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/88BFDD1E-E1C5-704C-B70E-1822A2EBC022.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/8A58F301-01AB-0E41-9FAE-E01EA43D93EF.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/9B1D90C8-B345-DA44-A00E-ACB64C768060.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/9EB2B375-7169-1C46-8CFE-A7317B1C57E8.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/A49B72E8-1230-204A-80C9-4812B16AFF6D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/A9C13572-2FBC-F345-A322-CAFC64C75866.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/AE3DCA3F-C36F-234C-B517-07069AA87970.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/BC72D35A-97A7-9742-80D9-6CC3F99E03A6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/D0FC8E63-DE86-BF4F-B2C0-2EB7B312165A.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/D54100B7-55CF-9C4C-BDE4-685BF33D4AA5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/E2D5F259-F618-C145-A73A-03964BA6DD56.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/E675D1A7-0AB6-5840-9F8E-D69B07370B24.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/F719CF89-5D5B-F042-A67B-ED95BB845D23.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/FB82E9A1-F132-CE4A-9573-57511A28B29E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/FCFD5CF7-4A41-1C43-A274-789A361F37E1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/FE066661-0DCB-754B-97C2-7C055C0D29E4.root',
] )
