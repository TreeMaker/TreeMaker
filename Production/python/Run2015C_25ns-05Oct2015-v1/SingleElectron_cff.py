import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/045710AD-C774-E511-9A9A-003048FFD770.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/221675AC-C774-E511-AAA8-003048FFCBA8.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/564B37A9-C774-E511-8E5F-0025905A608E.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/6AFCCAA5-C774-E511-89E6-0026189438AC.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/6E45BAC3-C774-E511-BB54-0025905B85D0.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/9CF475A8-C774-E511-BF1C-003048FFD7D4.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/C60660A5-C774-E511-B3DC-002618943867.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/CC6E5BBE-C774-E511-9785-002618943930.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/CCB9E8A4-C774-E511-8B2C-002618943983.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/E877FEBE-C774-E511-9510-0026189438E1.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/EC28D8A8-C774-E511-A1E8-0025905A60D0.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/30000/FA20D0A5-C774-E511-8F62-0026189438AC.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/50000/20F95D7F-3574-E511-B94D-0025905A60EE.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/50000/60BEE97A-3574-E511-B548-0025905B85AE.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/50000/662C127A-3574-E511-AB8C-0025905A60FE.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/50000/8EB73779-3574-E511-86E9-0025905A605E.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/50000/9C016C79-3574-E511-BC54-0025905A6132.root',
       '/store/data/Run2015C_25ns/SingleElectron/MINIAOD/05Oct2015-v1/50000/ECA5A177-3574-E511-B4CD-0025905A60B4.root' ] );


secFiles.extend( [
               ] )

