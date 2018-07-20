import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_1/RelValTTbar_13/MINIAODSIM/101X_upgrade2018_realistic_v7-v1/10000/4ED3B02A-963C-E811-8778-0025905B85C0.root',
] )
