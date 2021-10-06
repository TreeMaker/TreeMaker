import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/0B49C562-9ADF-9042-87D1-6D2D5D907F1C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/0DD81481-9800-4843-B9C4-BEE78C720171.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/26DD870A-5CDC-5A47-971F-9B9E8EFD456C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/2DD12D4F-E74A-9B47-BE5F-1090AD200ADE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/49B0ECC7-A0E1-8943-A889-F7E781F683DF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/4C815889-4C17-B847-B6D8-6A99282FC617.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/4DA714F6-6B41-D946-BBD5-80162B623D84.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/6B08A030-B8E4-9A47-B46A-926F09F20326.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/7D9C0CE1-AF31-EF48-BC4E-852444173B08.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/82683D61-19C0-AF47-BE6D-6C0A7BE82029.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/9C70D693-7B46-AA43-8DB9-CA716F02E529.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/A203180F-6496-414B-A15A-1CC2615E232D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/B4D73F3F-3671-DA40-B122-B94AFB5C92D6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/CB06E6D7-B026-874D-9621-B7D86F25FF95.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/DC48C67D-C769-7848-9261-5494C7E7CA48.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/E60D3354-D84F-604B-843E-B0294046F264.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/FFCB533D-7897-544B-B0DF-C873E342B440.root',
] )
