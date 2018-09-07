import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/00313A35-CA8C-E811-8991-0001010008C4.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/1AD48A41-C98C-E811-B216-000101000868.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/26F927EE-E48C-E811-AC7F-00010100096D.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/34A15482-648C-E811-85CF-000101000862.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/642C905F-BE8B-E811-8A11-00010100085C.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/70E883CB-CC8C-E811-8A9F-001E67F8F7AE.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/8CAC7C0D-D08C-E811-83B3-001E6739C159.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/B091AA88-918C-E811-8EAC-000101000970.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/C4F3F1FD-818C-E811-8F56-00010100086C.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/CACD4C5F-BE8B-E811-B0EB-00010100085C.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/17Jul2018_ver1-v1/40000/E81E6AE1-C28C-E811-8591-001E673D0679.root',
] )
