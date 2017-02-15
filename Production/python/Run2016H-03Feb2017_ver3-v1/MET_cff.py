import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/0EC2239F-8AEA-E611-9FB3-008CFA111218.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/2A9DE5C7-ADEA-E611-9F9C-008CFA111290.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/6AD62BA4-8AEA-E611-95C4-008CFA1979A0.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/A46A2161-7DEA-E611-AB70-008CFA197424.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/B046BFAB-84EA-E611-8175-008CFA11138C.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/C62DFFAA-84EA-E611-95DC-008CFA197A04.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/DCA957C9-ADEA-E611-AD37-008CFA111154.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/DE7C41A6-8AEA-E611-B09B-008CFA110AB4.root',
       '/store/data/Run2016H/MET/MINIAOD/03Feb2017_ver3-v1/80000/F40D929F-8AEA-E611-8021-008CFA5D275C.root',
] )
