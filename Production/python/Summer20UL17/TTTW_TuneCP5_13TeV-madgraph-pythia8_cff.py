import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/8F56C3DB-7CDC-3046-9AEA-7BED8620A384.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/90C68B9A-25DA-AB48-8D91-FEC92E0F0567.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/F33435FA-8878-DE4C-95CF-1DD02C42DBB4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/248184BC-F9D3-D649-9101-CC150A2780F4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/25391668-F773-A94D-ADB6-6A7FE4E5C08A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/39B43D47-5AFF-F346-853A-9F51567739A7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/6973E585-FCE9-0548-9CAE-DF563A44627C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/B307C30F-DA24-2E4F-A74E-5C17041A56C1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/C14BDBEB-1C06-024E-A6AB-0142B2332F6C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/C7D3AA01-85C4-4C49-B08D-AD124A764CEF.root',
] )
