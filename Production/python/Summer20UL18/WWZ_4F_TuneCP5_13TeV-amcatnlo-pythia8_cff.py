import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/01E36035-F087-4B45-9FD8-A358AC78933B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/0EABCC4F-C3EB-4B43-A93E-83FEE42ECB16.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/1292EC0F-9DF9-9747-A933-2E85EF1C62D1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/1F99D058-04C9-0645-885F-B34A2EF730A5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/29794BA0-B6CD-2441-A814-3E30E1095EFB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/37114A53-2C8D-7B46-AA02-C3371C808F9F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3D986819-6C8E-E745-AA18-BA6F2F5F8F88.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/3E1282C1-F3FC-AF4C-A736-137252FB7483.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/4F18C3AA-0A21-9E4B-B8B5-983E2D0B0EDB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/5F88E165-84E1-214A-A3DE-72BD235A9812.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/662EC995-C6DD-C045-986C-B61DF9AF0115.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/7EB9F65A-8C08-C84F-8C5E-627E161568A4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/996B7972-A318-394C-9E07-895A7CFDBBEC.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/9F101F16-3FFF-D64E-8779-B5DB3A2BBC26.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/A566571E-1C3B-DC44-BA6F-3D154840805C.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/A5C598B4-71AC-0541-B36A-A6A3A51488FE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/AFD987DB-E7F0-544D-A75A-2DA09137BA21.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/B1469658-A0CF-CF41-8F92-7D080E8FEDB3.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/BB03D4A9-A888-4D40-9F0D-49AF88C5C6AC.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/BBC9FDD7-056C-FA49-9A33-8522D0FF8042.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/CC6A4A04-8227-8B4C-B5F0-8E4C705DFF25.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/D35399A4-0DC7-554D-B58F-76309A57D0CB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/D7BCC38B-1B86-644E-9264-7F7031477198.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/ECC5E889-56D7-D64C-BAD9-2BF9D6F7B659.root',
       '/store/mc/RunIISummer20UL18MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/EFAF398A-5F19-D344-9B63-8C66288FA64A.root',
] )
