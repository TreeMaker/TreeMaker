import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/1967B356-99BB-BA46-A7EA-332C8E522F11.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/437AC46B-FC1C-4E41-8930-202B21A03E57.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/4AD914C8-5C19-7946-B205-86068FCBF85D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/5B260785-E7C6-E74C-9AE9-DDB68613B2E6.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/5F341644-B9FB-F745-94D9-67A28E0B3180.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/6C5D2DBA-29E4-9C4B-BDFB-A113278EC1A9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/7B043CCD-D2AF-1E42-A7D1-1B60070A8132.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/84230197-194F-D24F-A5C9-63804350F6E8.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/CA5C4716-B901-134A-BE13-254597D2C934.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/CC4233E2-C8BC-D743-9A22-4EF4BDE0B6DD.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/EAB6C866-71F5-994B-9434-474CFCE176BC.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/F111F4DC-3D82-9648-ABC9-4BDDA5EC5315.root',
       '/store/mc/RunIISummer20UL18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/270000/F48D9E3C-6529-9A4E-8601-D581FE2A99BF.root',
] )
