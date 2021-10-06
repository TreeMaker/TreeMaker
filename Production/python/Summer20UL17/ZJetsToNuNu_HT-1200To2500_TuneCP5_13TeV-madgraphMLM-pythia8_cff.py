import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/214CC732-77C2-D24A-9741-09DFED6B9C31.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/A2A477E4-43B5-0547-A75C-E5B3CECA815F.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/CE112085-5E9E-484D-B22A-310448443947.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/D040081E-C5F9-EA49-907F-4CFB3FCCD4DF.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/3A8EDD69-23F0-7A45-8B07-A5B80AC1C96D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/0E0FE3B8-F244-D848-BBE6-4D598CD1ED6B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/11213491-C285-5845-9A5D-9DC149F20EE9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/41AB87FC-4DEC-AA44-908B-8A3DE8B07FE3.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/5EE3C241-D397-F74E-AA29-5691B3207DB9.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/60638047-4850-3349-BF7B-5B21E7AE257D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/64209592-C26A-CD49-9FF5-30BB095259EC.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/F114C396-7EAA-E24B-A0C9-A69ECCB81E77.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/6FA1B7C5-E8EB-6D40-9A96-5D65D73C103B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/73179646-F797-8143-8CCA-9E2EEDC2015B.root',
] )
