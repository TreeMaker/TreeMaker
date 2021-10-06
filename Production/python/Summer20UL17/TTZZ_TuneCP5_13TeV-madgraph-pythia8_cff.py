import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/3D498AE2-3A12-8A45-AF44-84C68222302E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/67C5AFF9-FA21-EE4E-A239-54BDF7914A4D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/FBFB8D18-CE68-4540-8B33-BD8DFCF6B60A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/4C6D52D0-F435-6345-9328-ED96FD6355C0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/EE1D862E-B91B-F443-8A63-88DC2C2A996C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/140000/327AB10D-8ECE-3C43-9053-100896FD8E26.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/26403B4B-27FD-634A-8EB7-8000B41FDCBB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/32732A57-46AE-6A4A-9205-10DB97860A0F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/480DD3EF-08AA-D14C-AA21-7F78E8DD38C6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/72361C93-7177-E341-BE3C-3F23DB0CAB36.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/790E293C-0C91-C54B-BB32-AED716DC95C7.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/90CB9250-D330-2B4E-92A8-25C9F17132F4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/A9D6F2D6-8058-6246-9E86-DF611E243970.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/CD07AE04-994C-C741-BA52-9EEF9964F60E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/F1E4021F-5AAB-944F-AA41-8271093149BC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/FB8AEA28-0677-8949-9428-387E3A7CCBAC.root',
] )
