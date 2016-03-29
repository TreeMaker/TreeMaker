import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015C_25ns/MET/MINIAOD/05Oct2015-v1/30000/50C12865-FB73-E511-92A2-0025905A6118.root',
       '/store/data/Run2015C_25ns/MET/MINIAOD/05Oct2015-v1/30000/78337277-FB73-E511-A688-0025905A60F4.root',
       '/store/data/Run2015C_25ns/MET/MINIAOD/05Oct2015-v1/30000/F2BFBA50-FB73-E511-A59A-00261894391C.root' ] );


secFiles.extend( [
               ] )

