import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/D36750BB-8CE7-DC41-8303-D06D62635DE2.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/DE8CD2F1-5F98-1A48-82EB-B9F7C0BCD9FE.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/A712D8E3-784F-7C4D-A205-6710E05AB3E9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2540000/5F5DF255-57A7-C548-9E89-0422F3BDE190.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/1AF3E680-694D-694E-951D-620E9A7DAF5F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/444ADA22-0E29-4143-A612-2E067BA1DBBB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/CDA330FB-EC10-E441-B429-7BAAF0CF7ADA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/E128E2EF-324A-3D4B-94BB-833B475299DB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/365FC855-40FF-A54C-8244-41A5D7F46F61.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/964B5EA6-3233-2E46-9A59-219253096312.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/9D709156-899F-4041-8124-741D4B993EED.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/AE4BEFA4-F2C2-7E43-842D-740324B78069.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/B239A2AD-61E8-8F4D-86EC-F8288183E947.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/B92744F5-65FC-4046-AAD8-A282CA60E0DC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/D82BAACD-A834-154A-81A0-6CDFF9E757EC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/E7F640F3-83DC-FD44-A803-EBB5E37CADDB.root',
] )
