import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/0F39E7E4-896C-D245-A2AA-6DA55F7D53F9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/B82D2FC4-A2FA-044C-A11A-63AA1FA44DB6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/C804D8A5-00CD-C04C-A2BD-01501AD8ABB9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/66E3B1BC-F698-6342-B7CE-62BE47EB542E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/41B6B8D4-E014-3B4A-820B-2D6B91A28C46.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/5999074D-761C-2447-A90E-E588F563D3E5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/656C5587-375F-9840-A853-F95BC802E4B1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/95D76B38-F2F1-B24E-96E3-4D232D1D9FE3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/E025CA61-37DA-AE47-9ED4-323A1DC9C01F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/A4646810-6BA1-7C4B-BE7A-9BF3E14DDD46.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/F9B40589-D0F8-7C4A-9BF4-A6558C09E727.root',
] )
