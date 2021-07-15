import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/09A09FFA-8F9E-2245-A9E8-42146576F0E8.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/0D136BA8-BD84-C145-9596-D91757A8AD3E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/1177B342-7A24-8E45-A281-77FF7EF76090.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/14093C69-EC70-DD46-B84F-F11866D0F142.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/1FFC0464-B9DD-7D43-9571-BF7B82E29A12.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/20DAB710-7CFB-D64E-AD62-BE3D6E1ABF75.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/25A102D2-6055-0546-98A0-7AD8E55D2889.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/29ECD3A8-4686-AD42-9332-5D0F8956908B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/2DB4DD74-40F2-EE48-A810-272CA73CA033.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/34B3CFE1-0BE8-A64C-96F0-06AD933DC934.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/3FFFB13D-D3BB-2742-BE81-9ABBA3F61D18.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/51BF639B-BB32-EB44-98BB-53A96C84E7C3.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/58828203-8695-0C4F-ADEB-4460ED2D5E6C.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/61326C98-B057-FC45-92A3-A6DB4870554B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/6307254B-B68B-F94F-858D-A9B55B41B241.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/67BBE582-3C68-ED49-8382-43A2547B1EC2.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/6936244A-8B92-5A48-82A9-F4C55C2C3D19.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/6B0DF9DA-CACA-7E44-962A-ABE2F11E32AB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/701881EF-C234-5F4C-BF17-0AF837417CB9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/712D427F-3A82-5E48-B393-4D04E9B52B35.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/7A6380CE-B61A-5D40-B701-EA9056325374.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/9437661F-8439-D045-A628-FC1DD58B148A.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/AA3F206B-264B-B34A-AE96-BB4555A9C4CD.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/AAC0F188-B5CD-EF4C-BA4F-D174A86F2604.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/BBD40ACE-DCAE-9340-9BA9-159153E96869.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/BF7073A4-3F49-BE41-8CC3-22AC1672A5E0.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/C554EF74-ABA8-564B-BBF5-0470578A011F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/D8C36558-E989-9549-81BE-A5138267BE6E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/DCD7F1C5-9402-E444-A663-E92CE1CE312E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/EB38859B-1154-1B44-88BC-DBCD934C715F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/EB6730A9-1735-AF4C-8A3F-D96E024BB798.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/F26AC7FB-C42E-5B4F-8266-B42987522AE2.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/F96F45A5-EFA2-C840-80B9-D5D3885FF400.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v1/240000/FF183D48-C256-0141-9CC6-28D3AAB90AEC.root',
] )
