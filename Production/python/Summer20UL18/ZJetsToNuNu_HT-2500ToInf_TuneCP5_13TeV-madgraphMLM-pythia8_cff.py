import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/67C23F01-D666-6B44-BEE0-54BADC85DFBE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/6F0BAF76-DB01-3248-904A-935B10585617.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/DFD20634-83B6-0144-8DEE-5F890B884655.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/E5003DE6-1674-2049-BFF9-1A47277E1CDE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/270000/F80C5450-4D92-1F4D-9DEF-3E57AC5E7E3F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/8484387B-9F61-C745-B24E-FF9774A63A3B.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/91BA683E-6948-1F4C-881C-E47F881F33F3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/CC82A73A-3FD9-0247-9FCC-4EB167FA3677.root',
] )
