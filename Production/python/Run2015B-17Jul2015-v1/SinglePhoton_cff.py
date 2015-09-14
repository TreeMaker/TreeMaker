import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SinglePhoton/MINIAOD/17Jul2015-v1/30000/34DA98B8-C12E-E511-B09A-0025905A60EE.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/17Jul2015-v1/30000/36E477B4-C12E-E511-B76A-003048FFCC18.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/17Jul2015-v1/30000/649A02FE-C22E-E511-BA0E-0026189438EA.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/17Jul2015-v1/30000/7E24B0B7-C12E-E511-AB77-0026189438EA.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/17Jul2015-v1/30000/9AA235B1-C12E-E511-91BB-002618943902.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/17Jul2015-v1/30000/9C8F1603-C32E-E511-8EDA-0025905A608C.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/17Jul2015-v1/30000/BCDC1CB9-C12E-E511-AF02-0025905A48FC.root',
       '/store/data/Run2015B/SinglePhoton/MINIAOD/17Jul2015-v1/30000/E2C6A3F8-C22E-E511-877E-0025905A60B4.root' ] );


secFiles.extend( [
               ] )

