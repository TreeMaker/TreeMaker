import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/14E20156-6476-2A44-AB70-22F749E9AF40.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/2453575D-EBE2-F440-BF4C-B7D82324BA74.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/27189B1F-A8E2-E34F-A33E-DFDBCA3CBD35.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/48B062F1-19AA-4B4D-8458-CF0B1084AEA8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/5F185DD7-7968-5D46-942D-F6A298980ED1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/8ACA9DE8-A2A5-5948-BBEE-48F14617D9A3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/FD082A5B-B55C-194B-8D38-BF25FE745395.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/7874EBD5-BF59-7E43-A266-D9873668FBB9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/D5ABB885-9E96-4B48-AE89-B89A32E6F02A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/2A3CC9DE-3EB8-7542-8699-ED27BAF6D513.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B8319528-B8B1-5445-8ED9-6FE27D9049A1.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/D90A0027-F54E-184F-98C5-D640844F89D9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/693EF1A8-C733-644F-A20B-2E5E3776B64E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/A094C3F9-CA59-C649-98F5-AA4D66309100.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/CA5551B9-A074-5140-98B6-429A6CD9F45F.root',
] )
