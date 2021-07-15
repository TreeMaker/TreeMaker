import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/60913982-3D96-8940-B7F0-80F3C1BC6613.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/6AADC725-C26C-D840-BF9E-7784C0652FA4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/B4E6989C-B2EA-CB49-81F9-2A921089E7A3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/270000/EDF40366-A069-9A49-9CAD-18CEFF55D5E8.root',
] )
