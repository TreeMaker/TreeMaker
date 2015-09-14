import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/3226AF16-C22E-E511-B9D7-0025905A613C.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/365FCC3E-C22E-E511-9502-002618943849.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/48DBDEE4-C12E-E511-9E87-002618FDA28E.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/64E75A36-C22E-E511-A2D8-00261894382D.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/7C98C1FC-C12E-E511-8439-002618943982.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/8289C506-C22E-E511-9DB8-0025905A610A.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/A44418F0-C12E-E511-95A8-002618943971.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/BA824BF0-C12E-E511-8B1D-0025905A613C.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/C40D8102-C22E-E511-AF03-0025905AA9CC.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/D8ED75E7-C12E-E511-8CBF-0025905A608C.root',
       '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/F6F4BD01-C22E-E511-8631-003048FFD770.root' ] );


secFiles.extend( [
               ] )

