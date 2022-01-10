import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/3F0B3597-06E4-A747-87CF-4EF7D1B154EA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/4D7B86B3-76DA-5B46-A854-A61717E599A8.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/6B9BC76C-41ED-8347-8ECD-A7B038CCED9D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2520000/B63F7BD3-BCE4-CB46-9F5D-D0D7FE6902F4.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/0FF1B751-1176-5341-8B22-DD22C4DB33D6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/43D888AB-82C9-E640-B143-69F252CB474A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/97FB5530-24E4-2D47-A595-FE7E46690D08.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/9B7DF6F7-18F9-7A44-B4F8-FC6D87CD59B0.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/CD75A23C-4AA8-254B-9906-CD41BB17DB11.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/CE61E566-4383-BD49-ADF1-588AA9D78093.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2530000/F359FCB2-E040-244C-B05A-308350756A8D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2550000/17DADA3D-57D5-0A4D-9FC0-C239A394F4CB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/42FC877B-D666-5347-8F13-D64F394ACEA6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/55C62EEB-7D5E-9943-9A44-50E4ED794395.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/6805F9C2-4E0A-F740-9F8A-A80AD7767F0E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/793C7C2C-8419-E74B-9915-2B71EBC2908C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/8A02360E-B9E8-E041-8244-BDFD85F6A692.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B0843526-8F2F-9542-8092-07EA88FCA5A5.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B5B0A716-F6BB-9C42-A0CB-7D6BE0223A7F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/B6D599AC-5252-7D4F-8E3E-FB8B14D72573.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/260000/FDB58EAC-6764-2947-B083-AB6C6C4A423C.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/270000/32DFE072-2782-E045-A3E7-E69227817769.root',
] )
