import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/0D1F31F6-72A9-DD4B-ABE3-A93F7215ACDC.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/1EFDB4D1-D873-564E-9CD4-E571321E3511.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/35CC447F-A118-6B44-ADCC-19AE3D75374C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/4A3E7D4F-8811-7F4C-B590-6BE0C90CF297.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/4B5E8C9D-28AF-AA4C-ABE7-EB6FBEE291AA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/5353707E-BAA5-CC48-A8D3-A80B08B88B91.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/5F1C1C34-C982-1441-8628-1912479D5A62.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/67F1EEFE-E4D0-444B-99E8-4E9DB807D73F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/70A9FC40-3DAF-DA4F-A41F-98C7DD8C99F4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/7B9C4EEA-58E7-8147-9279-1A56900C8FF8.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/8B686718-CBB1-D545-8E30-642D47DBB421.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/8E28A415-E5C2-0E4D-B3F3-8C0B0BA70C07.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/984E55C1-5056-EF45-97B7-7BF838F73C9B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/9BFCFA46-2F82-8E41-B07C-723A8C919FA1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/A39EDF27-E69C-6148-B751-989863611D73.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/ACDB991C-37A0-3F4C-B5E4-E2F49E33B9E0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/AEE199DD-E347-7C4D-8B84-05578DA8BF54.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/B08A5E90-F2E4-7F41-9711-37B5E9C450C4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/B89CBF67-8EEF-9C4E-B81C-1A5B0DA7642A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/BA9448B2-9CD4-BB41-BC6B-6E53EDD7EFA3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/BB977A20-BB23-1146-A8BF-7395B4315CFA.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/BDDB409A-3EF0-6A40-8783-22257E8E6589.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/CCC60003-EE9B-A648-97B2-522B51EA4E48.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/CEA38B92-85FC-0643-9AF7-A2AAB79722DF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/D11CD8E1-64B7-B14E-9720-C800F868C459.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/D41CE315-3626-D849-8FF9-51C446C29545.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/DF38860C-D577-7449-B3B3-4AD30456D6BF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/E092905F-3F25-CC4B-B0C9-70A02142C76E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/E176014E-F240-B64D-911B-53C1BD9F8C1D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/E31313C8-512C-FD43-97CC-987FB38CD45C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/FA0B3718-1C81-0B4E-9FDF-CFEC00922D8E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/FB25D557-49E8-A046-A343-F9991F7CF695.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/452EE185-1EF3-6744-B6A6-B74ADC2FFD7E.root',
] )
