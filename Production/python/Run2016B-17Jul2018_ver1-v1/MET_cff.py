import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/MET/MINIAOD/17Jul2018_ver1-v1/40000/0A629636-3C8C-E811-A154-00266CFFCAC0.root',
       '/store/data/Run2016B/MET/MINIAOD/17Jul2018_ver1-v1/40000/1EBBE310-B08D-E811-88D6-AC1F6B1AEFEC.root',
       '/store/data/Run2016B/MET/MINIAOD/17Jul2018_ver1-v1/40000/1EE4D713-A98D-E811-8875-C4346BBCB408.root',
       '/store/data/Run2016B/MET/MINIAOD/17Jul2018_ver1-v1/40000/A0B4698A-628D-E811-84E7-00266CFEFC38.root',
       '/store/data/Run2016B/MET/MINIAOD/17Jul2018_ver1-v1/40000/E89ACA91-178D-E811-9C0E-AC1F6B1AF186.root',
       '/store/data/Run2016B/MET/MINIAOD/17Jul2018_ver1-v1/40000/EA786469-528D-E811-9A98-AC1F6B1AF1CE.root',
] )
