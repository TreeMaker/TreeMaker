import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/RelValQCD_FlatPt_15_3000HS_13/MINIAODSIM/PU25ns_101X_upgrade2018_realistic_HEmiss_v1-v1/10000/B46E1834-5880-E811-B31B-0CC47A4D7694.root',
       '/store/relval/CMSSW_10_1_7/RelValQCD_FlatPt_15_3000HS_13/MINIAODSIM/PU25ns_101X_upgrade2018_realistic_HEmiss_v1-v1/10000/BEE776E1-2380-E811-A67A-00248C55CC3C.root',
] )
