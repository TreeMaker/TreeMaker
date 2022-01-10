import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/472616DE-C107-3C41-8153-CDF36F01B4F6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/A9DC3619-ADF0-3841-80A1-6FBE344BF66B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/BB99EC1D-6D20-D44D-AEB0-1B24E92C2E6A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/DB4592B4-770C-DD4C-9CDF-EE41860A8145.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/19FF1C40-F0B6-964E-829E-3F9BB6B2249A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/6F391609-3BE9-114A-9FB2-287ED18469A6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/D3089052-4EC0-2146-8D08-C5C45B037367.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/F52382ED-70BD-B344-B274-B4F686B8AF05.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/07858B93-50EC-2F47-9353-7B29507FE234.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/6E6965A5-4521-4441-A541-10FF9C49571C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/C304B5AE-B483-3448-8605-EA29C72CE601.root',
] )
