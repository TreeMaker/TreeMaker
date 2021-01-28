import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
    '/store/user/lpcsusyhad/SVJ2017/boosted/miniaod/jetpt250_Sep29_year2018_mz250_epf30000_series7000/7000.root',
])
