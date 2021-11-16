import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/22E53878-15A3-6D4C-8447-99FE0B2A1B3D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/DC32BC94-0487-2C48-967F-8921FEACF5DD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2520000/F41F3084-1782-CA4A-BAB5-F447F2A67569.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/589D02F4-6507-1144-9493-FD1808241220.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/63EF0FB5-9624-DF46-A9EE-3EADB67FB2D8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/5811AD7D-B64C-6542-AAFB-9650EB34B08E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/937B5F12-96A6-1E4D-952B-AE854B6D0EF7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/3EFFBBCC-EF6C-844D-9031-215F3C579435.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/5140DD81-B282-6C48-9A4B-C3EDA1CA9B7C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/CAD72FDD-1877-C840-9A95-53A948AAF7E9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/ED4FC3D3-7B8D-E946-8C36-D7043C3DB209.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/F3FBF512-FD18-674F-847A-BBF0381D2B5D.root',
] )
