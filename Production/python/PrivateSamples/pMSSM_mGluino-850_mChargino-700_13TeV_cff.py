import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)

readFiles.extend( [
'/store/user/lpcsusyvbf/mc/r2.2015autumn/grid2a_850_700/evts_8aod_10k_74.root'
] )

secFiles.extend( [
               ] )
