import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_1/RelValQCD_Pt_80_120_13/MINIAODSIM/101X_upgrade2018_realistic_v7-v1/10000/EC917422-A13C-E811-9257-0025905B8610.root',
] )
