import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/HTMHT/MINIAOD/17Jul2015-v1/40000/9EF9D0DE-932E-E511-B0AB-002618943923.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/17Jul2015-v1/50000/4848A60B-992E-E511-9576-00261894397D.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/17Jul2015-v1/50000/5CFA3C09-992E-E511-9F8C-0025905964B6.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/17Jul2015-v1/50000/EE289108-992E-E511-92FF-0025905A6088.root' ] );


secFiles.extend( [
               ] )

