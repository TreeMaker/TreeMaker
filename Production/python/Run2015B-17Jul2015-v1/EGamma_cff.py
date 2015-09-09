import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/EGamma/MINIAOD/17Jul2015-v1/30000/EA67C8A7-A02E-E511-A4EA-002618943901.root' ] );


secFiles.extend( [
               ] )

