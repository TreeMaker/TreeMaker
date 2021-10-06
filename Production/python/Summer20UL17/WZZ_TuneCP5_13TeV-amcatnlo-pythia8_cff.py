import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/83A27B75-3B9F-BC4A-9A6B-1BEABE974ECA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/0DACB409-243C-DD4E-8376-6F2827D8CFA9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/1F476779-0C55-6347-8CF8-96110851C1FB.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/C39E0C42-3AD9-4549-A688-F2FC36046813.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/D083EC7F-89AE-AA43-9E89-67978856EB7D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/49122EF0-21B0-ED49-BA63-692FDB86AE3D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/08E0F358-B39E-0343-B1AB-09FA2593A582.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/4AD5B6BE-63B3-AF41-A28E-852F622309CA.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/693A65BD-69A5-B947-A1FE-4D611F9F0D37.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/7B548203-AF94-4648-8968-47B100FAD14A.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/A392078D-5675-E34A-B2ED-DA8EE9BE5C84.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/B95DAC31-82D4-0F43-8E43-2843FED597AF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/5DF752A8-0B27-1848-9164-0541C63DC77E.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/70000/FDD8A81B-4B51-8141-8D72-5D3A3A770B13.root',
] )
