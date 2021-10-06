import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/18516A88-C832-3140-B29F-5086D2C1D2CA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/23B723EB-62E6-9442-967F-914E87AEA352.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/30F14E90-3270-654B-98ED-44D4E7053BA8.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/4402A8B6-E03F-CF41-9406-3ECE3B2825C3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/48EEEA2B-4F39-8140-B179-24A3A8F9E27D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/4BA04838-C368-9D4D-ABC2-8A6D6D2E992E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/544DD6F0-AC8A-2846-A52D-4B4E7702929E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/89B944ED-56EF-1E4C-B031-96055D2C4E2E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/AE519068-21B4-814B-9E63-D9685BAC169D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/B6E1384B-F8FB-0C41-BD18-BE2F07315385.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/C13ADEF5-EAB8-EC40-8A7D-0BE94F214DEA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/130000/D177A06A-93D1-0141-9D99-F5660E4D6514.root',
] )
