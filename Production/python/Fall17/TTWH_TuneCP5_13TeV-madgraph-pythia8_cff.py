import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/40068400-3444-E811-8013-001E6779263E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/46119979-FF42-E811-8EB7-A4BF01125B00.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/4A051BEE-D442-E811-9ACD-001E67E6F882.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/BC969F4D-A242-E811-AC63-A4BF0112BC8C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/D0F2ACBE-EA42-E811-A813-001E677924C6.root',
] )
