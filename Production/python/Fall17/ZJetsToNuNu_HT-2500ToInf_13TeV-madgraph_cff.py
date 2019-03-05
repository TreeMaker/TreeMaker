import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/CC3CB693-7359-E811-87BA-FA163EC07F56.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/0E900A50-7859-E811-885F-FA163E4DAB5E.root',
] )
