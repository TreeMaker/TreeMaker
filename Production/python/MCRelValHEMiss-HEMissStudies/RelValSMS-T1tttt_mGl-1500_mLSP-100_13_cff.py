import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/RelValSMS-T1tttt_mGl-1500_mLSP-100_13/MINIAODSIM/101X_upgrade2018_realistic_HEmiss_v1-v1/10000/D853DD4C-B87F-E811-9540-0CC47A4D7626.root',
] )
