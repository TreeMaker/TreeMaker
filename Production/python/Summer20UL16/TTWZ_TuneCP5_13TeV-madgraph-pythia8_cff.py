import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/3EAC8D8E-1BD5-434C-9D85-D7E2C13D84D0.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/40D53B75-11CF-2B4F-86A9-F4EFC39FD838.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/67111EE0-6476-2C42-BEA5-2E21DE369901.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/9A13CBC8-5458-0F4E-9423-E161E1259546.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A153F550-531B-7745-9688-69F2767D8AE6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/A32366A8-204C-1D44-8266-F25ED710436F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/270000/B7841D91-9A2F-F24A-94F4-22AC01B80C84.root',
] )
