import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/197A5792-3B28-1E42-A69F-412736D88978.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/3D6438D2-114C-A74C-AF6E-DFEF633996AD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/0D631A9B-0B59-E848-9E97-DE46F81F351D.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/1EE7F510-AA66-3346-9945-04346C0F18BD.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/DCE338BF-BF13-FB49-BCEB-062EDC38CAC3.root',
] )
