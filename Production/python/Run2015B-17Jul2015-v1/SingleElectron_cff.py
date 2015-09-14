import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/109023E8-C02E-E511-8913-0025905A610A.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/18EA30CE-C02E-E511-AAAE-0025905B859E.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/1C847DE8-C02E-E511-8D41-0025905A60DA.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/3861A09F-C02E-E511-B4B3-0025905A613C.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/3A979A2B-C12E-E511-A5F7-0025905A48D6.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/3C61DCE6-C02E-E511-ADD1-002618943971.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/3E4B2930-C12E-E511-872B-002590593920.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/48C83128-C12E-E511-B235-003048FFCC0A.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/4A52C8E2-C02E-E511-8FF3-0025905A60A0.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/5097CCE8-C02E-E511-B31C-002618FDA28E.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/52D4A025-C12E-E511-89FD-00261894382D.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/584065EA-C02E-E511-A27B-0025905A613C.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/58C331BE-C02E-E511-A2B2-0025905A608C.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/6012E4D2-C02E-E511-A24C-0025905B858E.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/6CFFA52B-C12E-E511-B60B-0025905A60F2.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/783F7796-C02E-E511-ABBE-003048FFD770.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/7E1814E8-C02E-E511-8E7E-0025905AA9CC.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/9261D028-C12E-E511-BBBF-0025905A60B4.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/96D4049C-C02E-E511-92C9-00261894397A.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/B2000C33-C12E-E511-BD6C-002618943849.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/B6D0E4CB-C12E-E511-AA9F-0025905B85AA.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/C68F6A2C-C12E-E511-8407-0025905A48BC.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/CC503EEC-C02E-E511-93A3-002618943982.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/17Jul2015-v1/30000/F40EF063-C02E-E511-A074-0025905A612A.root' ] );


secFiles.extend( [
               ] )

