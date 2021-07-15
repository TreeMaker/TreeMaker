import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/077DF477-59E3-5E4A-9224-542C4E3FED9E.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/1136D43F-6C30-664D-8ABF-78668EECDB3F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/22A0B58C-AD55-C44E-B0D7-194B2C7A3E44.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/2D16B98E-A139-DA45-892C-7195DE1AB03C.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/2EAA19B2-95FA-5E45-867F-699BDB0A61AA.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/3E4FBD6F-DBF1-E047-8C67-503E7DCB0FDE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/415E728B-56A7-F441-91E3-862C577CCD0B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/4C68AEC6-36ED-4747-8F7D-B747928C54BE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/548D65A6-0D4E-CC4E-B20B-76A38A90A921.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/63233226-73B1-CD44-BD78-3D02F6317A62.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/632F50D4-9AFE-C14D-83F7-ACADE813AE08.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/6F0F73F8-7678-E34B-B90D-E2712F853430.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/73CB85FE-1624-1C43-B53D-779711308D8A.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/9A7D0A92-729B-FF4F-BE2A-3A586CCC5FFC.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/9C038F79-5E69-914F-8D44-DC9C1098DF4B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/A8A7EEBD-37AE-3E4E-8D8A-95DEB5D0BE41.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/AC21E99D-9F39-AB41-B5DC-22DA4575B7F1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/B30AA970-166A-864C-8568-F61239520B44.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/D82F5C8E-4AEB-534C-B117-0B0899BE82CB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/DB755126-E222-EE49-B1BD-6813884537FB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/DF20DDF8-ECE0-574A-9BA8-0D61818C09BE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/EC105CDE-C815-2943-AF1F-DD4FFE89C29B.root',
] )
