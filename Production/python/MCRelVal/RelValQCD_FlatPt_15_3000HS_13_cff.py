import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_1/RelValQCD_FlatPt_15_3000HS_13/MINIAODSIM/PU25ns_101X_upgrade2018_realistic_v7-v1/10000/8AB99B35-193D-E811-B7C0-0CC47A4C8E2E.root',
       '/store/relval/CMSSW_10_1_1/RelValQCD_FlatPt_15_3000HS_13/MINIAODSIM/PU25ns_101X_upgrade2018_realistic_v7-v1/10000/A4206213-FD3D-E811-AD52-0025905A612E.root',
       '/store/relval/CMSSW_10_1_1/RelValQCD_FlatPt_15_3000HS_13/MINIAODSIM/PU25ns_101X_upgrade2018_realistic_v7-v1/10000/FA6FBFB6-E83D-E811-AE1D-0CC47A4C8E1C.root',
] )
