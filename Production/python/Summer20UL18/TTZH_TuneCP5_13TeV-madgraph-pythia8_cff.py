import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/128BB057-F439-FF43-BE0D-9D17A5122EC1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/34B209D8-65E8-AF4B-A354-70108B365212.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/4B1FEEF8-842C-5A48-AD6B-A90089F8335D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/8EA10A08-1014-B74E-AD62-3D7E4DFEAE93.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/AB058DC7-E9E9-EF4B-8C21-C6AFD6885C64.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/CE8F9B75-97A0-1741-8ACA-D232F9992CCF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2520000/FD18F4ED-D7D4-454A-8415-0A18E0AAEBFE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/B16053E2-3D97-E946-8241-8113465421AB.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2550000/7DE28F3A-1346-E144-9F09-00E4E7DCF649.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/056119FB-1194-2A4C-88C9-C8403BC7BF14.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/3640CBEE-BF3D-F04A-882D-BA1E783E8CA2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/74942593-0DB2-9A4B-9973-B9BBC25D7FA1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/AC06BAE9-03F7-AC4E-A9CD-2EE142EAFB20.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/C570D52D-6175-4442-AD72-EBE1F3E84CAF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/260000/D727556E-F32B-5549-AF92-C569E21133D4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/0334AB3C-B497-234B-8889-033AB55B7517.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/1EA9C117-1A97-C848-8604-3BFD5D936C7F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/9287B47A-AB7A-7144-B1EB-7604116FFD5F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/270000/B8D40138-3A2B-534E-974C-B61661AA6F57.root',
] )
