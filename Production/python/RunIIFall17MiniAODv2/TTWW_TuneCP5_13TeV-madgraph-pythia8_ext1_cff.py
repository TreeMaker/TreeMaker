import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/90000/32390DDF-21AB-E811-AF28-002590E7DE36.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/90000/962D3C05-2AAA-E811-91C8-AC1F6B0DE296.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/90000/9879C4C6-54AB-E811-AC4B-002590E7D7E2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/90000/E0E5B3FF-04AB-E811-A941-002590E7D5A6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/90000/F2C9EEA7-63AA-E811-82B1-AC1F6B0DE362.root',
] )
