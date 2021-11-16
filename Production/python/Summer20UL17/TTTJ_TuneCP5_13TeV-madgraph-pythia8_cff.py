import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/BF92C93B-762D-AB49-A596-52AF9C4910D5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/3CC32BD2-606D-F146-A63A-643F1FCF7C28.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/756A66E0-3886-B541-8394-868506C5090D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/B4BCBF68-99F1-1445-8EB7-E87BAA8C5C39.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/EFA99EF7-0843-E647-9E46-DCAAED1DE574.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/5051C2E4-654E-9743-AEBE-CC0375A99E6D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/79795FEC-5B16-2B4A-9423-EEDDCC6C44F5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/9B1D1A62-B937-9347-B1B9-1A5608F82320.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/186D00F1-C1F4-F54C-A4A2-817B0F30CFC9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/1D70C988-C6C2-7F49-B191-22DDF83D8CB4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/3383BA84-0401-0949-8432-9AEF70E0BE6D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/46CFF655-77C3-EF4E-9CA7-A954A916BD5D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/4F9C9985-2F53-8548-B907-EBA2FD097052.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/8B97E2F1-E90A-E84E-A70C-D7F24E108DDA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/B86ED3D5-DF9D-0448-B533-BA77E88C7C58.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/ED0DCF49-9FC7-6644-BBD5-7935EA50C394.root',
] )
