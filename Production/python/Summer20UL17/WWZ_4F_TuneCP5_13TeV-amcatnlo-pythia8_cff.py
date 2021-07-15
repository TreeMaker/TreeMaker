import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/114B6647-BD79-8447-BE7D-41E99C9B01DD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/1312E7E8-E757-7848-A515-36B232F67469.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/24E38382-3176-4549-A188-7B475A01A3C9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/26A05548-EF0D-3A4B-9335-724EF046B24E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/38F4E6B9-CC2C-7142-8416-E3EF3A9C0410.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/396C189E-CE18-0249-BA63-955E3BE298C0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/52011E45-54B2-784C-96B1-9A5E1EF2CDA0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/576ECD4C-9626-4141-980E-67E0B9AF1B70.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/60B06AD3-A96E-8741-8B00-0899F4544854.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/617855C6-3DE6-3245-9D59-1BF98491C845.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/61DB5BFD-C7AD-D240-8F30-8F0F883A539C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/6671B83B-0460-D645-AFFF-5BC8319B2E56.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/936B3A57-3373-2546-BA86-CFAC0EEC225A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/AE58E3E7-874B-5847-B768-7BBF92EB2974.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/B5622B8C-8EAB-8143-83BF-2477406EAB9F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/B6B24C3C-D2F7-D34A-9428-4C0DCC19ABB5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/BBEF4A1F-2FF3-4B41-8C3E-C557E675FF44.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/E28D43C3-395C-2D49-A2F6-84A89C1A8475.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/E4CD0F3A-5059-C248-9822-BB890AE1C57F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/F10C2427-638F-ED4C-9FD3-32E2702507DF.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/FA0F185E-02E4-C249-94B4-A59A20DAFAA1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/FAD721BC-C1FC-194E-B35C-79FD4DDFD002.root',
       '/store/mc/RunIISummer20UL17MiniAOD/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/FCAEFC2D-18E6-4F4D-8643-72AB2C414E23.root',
] )
