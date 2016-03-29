import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015C_25ns/HTMHT/MINIAOD/05Oct2015-v1/60000/7A9FE2F0-F873-E511-A536-0025905B8596.root',
       '/store/data/Run2015C_25ns/HTMHT/MINIAOD/05Oct2015-v1/60000/A0B62AEE-F873-E511-9E2F-0025905A60C6.root',
       '/store/data/Run2015C_25ns/HTMHT/MINIAOD/05Oct2015-v1/60000/C0A300ED-F873-E511-B438-0025905B85A2.root',
       '/store/data/Run2015C_25ns/HTMHT/MINIAOD/05Oct2015-v1/60000/DC2076ED-F873-E511-B625-0025905A60C6.root' ] );


secFiles.extend( [
               ] )

