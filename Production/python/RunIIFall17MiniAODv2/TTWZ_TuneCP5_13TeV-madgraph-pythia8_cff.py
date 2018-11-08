import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/48A86083-9F42-E811-ACC0-002590E3A004.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/56796D7C-6F42-E811-BA5D-0CC47AD99146.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/8AEE0A89-A342-E811-B334-0CC47A13CB62.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/90BE936A-7742-E811-B12D-0CC47A3B0508.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/A4EF4E14-AF42-E811-A97A-0CC47A13CD44.root',
] )
