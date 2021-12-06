import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/0780A5DF-4F0F-E648-ABC7-8C6E81713E76.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/97A9A3DF-CB5F-8C43-B5A3-46B32C54F47F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/166E9F52-9CB5-2D4C-B527-734A88644F89.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/596D4C9A-F4A2-7F45-A39F-11A90CD9920F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/B8D9A180-6B50-394D-BE3B-26FBBF0CADD3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2540000/E67F38B0-AD53-2743-B18A-F4E22FA796A9.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/16587B18-0EEC-F746-833B-62E3F8808BAA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/20CA18CE-6256-0B47-9619-82301BAF8DAF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/53C541EE-90B7-AF4C-850A-E58B9C5B8038.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/5FDA4CC1-C59F-E047-A4E1-24BC6DA7F5B5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/7C77F747-7038-C144-984F-A3B865DD38B1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/88A84EDD-9108-C34F-B299-F8E03A8D4F88.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/8CAFBFB1-4844-A144-BB7F-2DFBEE6C5FF5.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/961B1269-66BA-EC4D-ABE0-F2E95258E783.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/ACA35764-DF17-994D-92B3-2248F481292A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/BE9FE4F1-0410-1E49-8180-931AA0E4DEFF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/C82204AA-BAFB-3B4F-9F21-6A24C0E84986.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/F506B23D-880A-8147-B881-D644177DA219.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/70838389-457C-BB42-ABC9-EB055AF3AEF3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/A5789718-C16E-1246-AC48-968E89713079.root',
] )
