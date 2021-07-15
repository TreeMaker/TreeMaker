import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/016E1E96-F177-D94C-BB19-B3AB073083D4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/06ADFE32-D017-EB4A-B4AE-C42A16824D10.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/1662030D-5181-EF44-93E2-B5E4E2E0024F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/19BB4E73-2BC0-EB4B-A5F2-BC438C8CCDB1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/2363EEAF-D0BE-5D4B-9C25-215D4976DAA0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/27B557B0-1E9C-5E46-A18E-FE7A2C32D057.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/2E30A41F-4910-2B46-BB16-D93FF3651E42.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/33CA7CCE-B341-B848-9620-2C0A0FF85E2A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/4A1CEDE1-6C69-7842-9850-8BCC71DB6235.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/51B7132C-07AB-CD43-9242-F3B09D6102F6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/594D8B2E-B3ED-7E44-9335-7BCC08CEB6CD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/5E3CC9E0-02EE-5941-A127-9B64634C5A4A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/806CDB54-8A3E-9341-8E2C-B1F709F26349.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/8DA4ACD8-12C5-754F-9870-8B685B319059.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/91603E22-9032-E449-A8FB-A0E19995016E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/98A6AD5D-65BB-7D4F-814A-6868965BD00A.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/9E55D6A6-6FA4-CD41-864E-4D4C43AC1F84.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/230000/E510C874-CEAB-364F-BA9D-F850FA6CA9EB.root',
] )
