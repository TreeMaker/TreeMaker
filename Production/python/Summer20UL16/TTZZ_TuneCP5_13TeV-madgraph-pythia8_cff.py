import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/3D2D2830-4BAC-ED4E-B077-4456407A6BDE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/451B31C9-F2D9-F340-BB5F-A2B2887380B4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/795F6D4C-2CCE-EE4C-952C-07AA99249E5D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/8DE1426E-1128-A342-BA47-B5C36A5CBE68.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/D155F695-6B4D-4440-AFDE-D179BD85ACF7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/DE2E339B-995C-0945-AB9C-D58BE3022D59.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/F691E852-E428-B147-B750-3BF242A75D89.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/7B9AC9FF-6793-214F-BC48-B0326D3AA33E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/9A89BE6A-75FF-0348-8E06-3A6D0696289F.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/DB198E2F-FDCF-2F4E-9DE9-AFA746D701AA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/EEA694C4-CE46-2945-858C-CCE505066454.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/F3E38598-FA94-2C4E-A6D3-5F186DBC42B7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/4E53F30A-3783-0741-A7B2-38C180BD1BC6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/A0C5A832-17A3-B748-8AF4-6AE69B6CCFB6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/EF1CE6E1-A2A0-7740-813B-0707015A809A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/0C7064C9-D630-5B46-900A-90F5CABE47DD.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/279E6F92-BCA1-8E43-BD66-0B7A485B8614.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/80D3D002-82A9-364A-B345-DCCA97E29ACE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/C9421BD1-4A0A-154B-B0B0-F1FF20372C07.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/CE45934C-8B6C-A845-8565-8D49F030B4E3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E619471F-2774-7549-B85E-B8DFB3CB3D38.root',
] )
