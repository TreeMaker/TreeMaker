import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/6C750F06-BE8C-AC4F-9E2D-48D90EF3A4E2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/F518BC94-D8D8-F741-84CA-732E51C4537B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/47A86564-8A08-6848-AC62-972AF8DDCE49.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/FA227EA4-1BF6-0F4D-91C7-86F3CDDB6DE8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/71FA0108-1D86-9741-B4CC-B804F10F2937.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/9B12CEC6-7E98-F846-940C-ED99E619127F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/DF19A438-0E52-1E43-BF4A-73852E2B3143.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/E8D3FAD3-CEAC-8D4B-A5D4-C65627135A60.root',
] )
