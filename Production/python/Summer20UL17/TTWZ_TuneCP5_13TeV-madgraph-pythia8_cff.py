import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/ED9C84D1-E393-2742-B1FB-B2B602BD02B1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/0C0FB180-AD5A-A148-A4E5-C589BF535592.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/26ACD8CE-242D-FF45-A050-676E541E0374.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/34C07277-009C-A841-A1A7-476A92C77754.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/3D1A8070-F0F8-524E-A3DC-FA979609A538.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/79ABD722-1154-124D-A3AD-FC6FC22B490F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/CEAB64A8-E898-BE43-8674-04048B788F7C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/FE4BD402-ACAB-D447-9B02-39C995D38F8F.root',
] )
