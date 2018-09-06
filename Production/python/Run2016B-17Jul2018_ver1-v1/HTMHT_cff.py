import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver1-v1/50000/1465CE41-788C-E811-8FF9-0090FAA575E0.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver1-v1/50000/1CDE90F3-6E8C-E811-B7AF-0090FAA57910.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver1-v1/50000/8A05E7B6-7E8C-E811-8B90-A0369FE2C228.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver1-v1/50000/A6E66E51-788C-E811-80C9-A0369FD0B3EC.root',
       '/store/data/Run2016B/HTMHT/MINIAOD/17Jul2018_ver1-v1/50000/CAB4FB59-788C-E811-945C-A0369FE2C068.root',
] )
