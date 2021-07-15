import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/0F40FBC8-849F-B142-BDE2-E915F36FAB02.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/22225693-DC57-4740-9BC8-3104DB593BD1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/3B3437C7-45F6-AA4E-8B28-49B03F929206.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/4198C553-93C2-F24C-97A9-BA4B5DA0EA7E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/69305BB0-95B7-1748-88ED-0E5407362D5F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/76C6006D-834F-5A45-95CF-1D4E65FC99DD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/992339D4-5EC2-C040-BCAF-291FCDD12DB8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/ADD7C411-D014-FA44-8B01-5F63EE205CCD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/BA8554E0-F341-B94F-9461-91151B695BD8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/BC00A2DB-D37C-C14D-A277-50FCD0ADAEB1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F0D01B90-262C-4545-8FD7-DC8F2430FA2C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F96B7487-AAFF-6A41-938A-2FE043634DEE.root',
] )
