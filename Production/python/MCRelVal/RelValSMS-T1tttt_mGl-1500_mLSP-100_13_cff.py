import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_1/RelValSMS-T1tttt_mGl-1500_mLSP-100_13/MINIAODSIM/101X_upgrade2018_realistic_v7-v1/10000/FE293C51-973C-E811-8138-0025905B8582.root',
] )
