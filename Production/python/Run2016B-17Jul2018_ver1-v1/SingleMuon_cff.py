import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/20000/A04121A8-F29A-E811-8A5C-0242AC1C0500.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/20000/F846D019-069B-E811-A03B-0242AC1C0502.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/180C2061-0C8C-E811-8972-0242AC1C0501.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/2ECBF2B4-1A8C-E811-80A1-0242AC1C0501.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/306DAB6C-068C-E811-9E30-0242AC1C0501.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/382B7F0A-158C-E811-BD7A-0242AC1C0500.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/3A6CBD55-208C-E811-BE87-0242AC1C0502.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/427155EA-318C-E811-8E83-0242AC1C0500.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/46304C83-578C-E811-8B8D-0242AC1C0503.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/4AC0F170-268C-E811-9D11-0242AC1C0502.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/60D7731B-228C-E811-ABB1-0242AC1C0500.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/786C9D12-098C-E811-BE75-0242AC1C0502.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/82038504-248D-E811-AB09-0242AC1C0503.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/9A630671-0F8C-E811-8558-0242AC1C0504.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/A45CF911-238C-E811-8033-0242AC1C0502.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/C0057E83-178C-E811-BA61-0242AC1C0502.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/C63563D8-108C-E811-9394-0242AC1C0500.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/EE2A5AF6-248C-E811-996E-0242AC1C0500.root',
       '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver1-v1/80000/F2494388-1D8C-E811-BB8E-0242AC1C0502.root',
] )
