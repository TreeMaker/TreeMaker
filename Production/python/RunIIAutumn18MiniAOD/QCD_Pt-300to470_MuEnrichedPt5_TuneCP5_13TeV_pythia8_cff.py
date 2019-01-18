import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/10000/A7C980C0-2D32-BE40-B129-FA1A036F344B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/0007B3A9-8B5F-464F-AB64-3DD406F2F22B.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/12DC11CC-A686-2546-885B-D15C5BE08450.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/25D67657-8E06-AE48-BADE-B97E67BEB56C.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/29095FA1-E402-C547-B6A1-67A1753ADC08.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/3114881D-F6E1-F947-9076-D26B1AD061DC.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/3B7E8DF0-DD60-454D-92D7-CA6B31C25C55.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/3E224905-CC02-4E4A-970C-14F6276B0FC5.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/4CCECD9F-0B4A-254B-8F60-6007DCFC6B66.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/586B83D5-B0DC-EE4B-846D-24765BFB5F40.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/5A0D5A5D-6BF5-FF4F-B50E-9D506C10E091.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/674FA5DE-B600-AA4B-84A7-C6A2488860FF.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/6CD86350-4A1A-0940-A7E4-44B3A73BDFE4.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/725C2D6B-5B3E-D940-8EA2-9A7848D11F1A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/7966941D-444F-AC49-A836-23A7D2FD4365.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/8A807640-F2CE-0D45-9C99-AD660E0CD5C3.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/AD1A4EA0-DC24-D44A-8C3E-4A9A4E2C85E5.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/ADBD85DA-EF8A-2F4C-B1C4-E7965965C7DA.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/B2F2C973-44B6-1946-AF39-2292FCF126C7.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/B8CABEDB-11BC-E149-8CC5-71A5FB14FE68.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/CAB05DB5-EBA2-A141-9309-CEBF0078092D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/E74BF27E-A714-AB43-BACA-1740930FAE86.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/E7DAB5A8-7DCC-7C43-AF99-7020233A5DDC.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/EA33EC32-F9E4-DA40-A422-E0F7BC1C0861.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/EB095332-1FD1-FC40-B925-47A5C589947D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/270000/F62C8FD7-1EE0-D940-A49B-10602491BEE6.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v3/90000/749D3DEE-07B4-D647-98A5-AA98495562DB.root',
] )
