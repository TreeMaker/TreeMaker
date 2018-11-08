import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/142DCD6C-4744-E811-B136-0025905A60D0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/6A5BF8E6-1D44-E811-AD8A-0CC47A78A436.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/A87A99CA-2C44-E811-B3C7-0025905B85EE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B46DE7CD-1344-E811-A1E0-0CC47A4D7604.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/DE85B7F4-2544-E811-B388-0CC47A4D768E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F08BF000-CD44-E811-9133-0025905AA9F0.root',
] )
