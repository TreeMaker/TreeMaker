import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/RelValTTbar_13/MINIAODSIM/101X_upgrade2018_realistic_HEmiss_v1-v1/10000/86943A7E-A97F-E811-B61D-0025905B85F6.root',
] )
