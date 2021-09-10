import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/0A6E211D-0937-3342-9525-4BF0551BFA02.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/14F4BAD8-4DC4-AC4C-8110-60DCAACB843B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/47C0FF33-9783-344E-9F20-A037AD43F327.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/3BCB1572-93D2-F74D-9784-375613040D42.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/23E1A8B3-856E-F747-A97E-C3C0214E43ED.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/C4B1AA37-89DB-7A43-8C30-1DF1DD0B68AB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/4ABF7DB7-F6FD-1F4C-8F96-6B39C0F2E552.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/5A534DD3-D4C1-EB45-9632-301C94B812FC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/6E3C21FC-ADA0-5A4A-A17F-0F84DB4BBD77.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/C2FF9A6C-7734-FA46-9CAE-3A316F775A13.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/F1BA7891-69ED-F14E-89CE-AC8896A0014E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/10AE1878-A1A3-7D4E-9F9B-937A8E6F803A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/1B8479B3-CFD0-EE4E-B4B2-0F9F2DE0D5B7.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/3D417F4C-D2E3-2F48-A244-97426B914C2A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/A759A843-7C82-5545-861D-73E99AC212FC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/A88219D5-0DB3-6A4A-903D-8A6DF1BA5393.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/DA038B38-9E13-374C-A0AA-8C75E8A28CB1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/E516E075-78BD-DF4E-9531-4BBF02138223.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/EDD7719A-BC67-0E4B-BBE7-4E98E52F238A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/70000/F075DB20-5ED6-A942-880A-67FE2F6514AE.root',
] )
