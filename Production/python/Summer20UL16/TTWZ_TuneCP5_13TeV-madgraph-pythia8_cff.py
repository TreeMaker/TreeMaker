import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/79CAE5E1-3215-D047-B940-DFD97247D8DB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/7AD014BA-0DB2-EF49-AEBD-3F066614F971.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/A63C661C-EB35-B24C-83C0-29E9F72A4589.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/F74FE799-E534-6A4C-9EC6-9FCB38F10DB5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/FB14D6C0-670A-6B4C-BDBE-AAB90E605DE0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A917ACE9-219C-FA44-99D8-654E5081D377.root',
] )
