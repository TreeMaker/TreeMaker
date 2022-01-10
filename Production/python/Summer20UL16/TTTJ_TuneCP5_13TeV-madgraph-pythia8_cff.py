import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2530000/280BDB89-006C-7346-B450-3E3DF083357E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/209E7BD5-8DAF-6040-8AD6-C84037F7ACA0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/58CAAB0E-7899-014D-8498-8EECD6E326D2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/834603AC-B2FD-1B45-A165-C0040C8D34C1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/DEAD80DA-75AF-4B4A-9C02-BC6769F63BD7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/64C4F703-3CA1-E44A-9184-6D60E91AFB97.root',
] )
