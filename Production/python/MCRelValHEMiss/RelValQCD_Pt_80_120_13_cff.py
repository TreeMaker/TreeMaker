import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/RelValQCD_Pt_80_120_13/MINIAODSIM/101X_upgrade2018_realistic_HEmiss_v1-v1/10000/022859A8-A17F-E811-9D71-0CC47A4C8F08.root',
] )
