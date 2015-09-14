import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SingleMu/MINIAOD/17Jul2015-v1/30000/2A451E44-BE2E-E511-AFBA-0025905A613C.root',
       '/store/data/Run2015B/SingleMu/MINIAOD/17Jul2015-v1/30000/5C72874E-BE2E-E511-A6D5-0025905A6090.root',
       '/store/data/Run2015B/SingleMu/MINIAOD/17Jul2015-v1/30000/7ED26990-BD2E-E511-B519-002618FDA28E.root',
       '/store/data/Run2015B/SingleMu/MINIAOD/17Jul2015-v1/30000/9AD4F3EC-BD2E-E511-8494-002618943981.root',
       '/store/data/Run2015B/SingleMu/MINIAOD/17Jul2015-v1/30000/B0B42589-BD2E-E511-99DE-0026189438F5.root',
       '/store/data/Run2015B/SingleMu/MINIAOD/17Jul2015-v1/30000/C8681E8D-BD2E-E511-AE59-0025905A60B4.root',
       '/store/data/Run2015B/SingleMu/MINIAOD/17Jul2015-v1/30000/CE954B54-BE2E-E511-8C94-0026189438F5.root' ] );


secFiles.extend( [
               ] )

