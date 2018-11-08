import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/264B34BD-9342-E811-848E-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/9606C63D-6042-E811-AFEB-0242AC1C0505.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/C4A19CC0-4C42-E811-A5E4-0242AC1C0508.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/58C0E383-F842-E811-AB69-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/82CCC6C8-0843-E811-B974-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B44B6427-7F42-E811-8E46-0242AC1C0500.root',
] )
