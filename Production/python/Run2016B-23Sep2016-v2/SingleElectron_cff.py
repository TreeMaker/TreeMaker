import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/08A02DC3-608C-E611-ADA5-0025905B85B6.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/0C9C7188-708C-E611-A4D7-0025907DE266.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/14415255-6B8C-E611-87D3-002590E3A212.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/1C8FBE37-DA8C-E611-8C09-02163E00BC44.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/323FD764-608C-E611-B280-008CFA166038.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/3A4E0925-F78C-E611-97B7-008CFAFBEBF8.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/56922070-FE8B-E611-97A0-0025905C2CE4.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/5A4402F5-638C-E611-A471-0025905A60AA.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/6819AF5F-DC8C-E611-8721-0242AC130003.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/7AF28141-6A8C-E611-AE65-0025907D1D6C.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/866356B0-DB8C-E611-95CB-0CC47AA99436.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/8EC4330F-FF87-E611-B2D4-008CFA5D275C.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/907DC206-DC8C-E611-B91C-0CC47A7C3572.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/90D0CC35-648C-E611-AF6A-002590FD5A48.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/9606A45B-128C-E611-9935-001D09FDD7DA.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/984A6C0B-1D8C-E611-AFBA-0CC47A4D7634.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/9A0E4119-0A88-E611-A5BB-0CC47A1E0C76.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/A00E944D-DC8C-E611-8FCB-008CFA110AA8.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/A439B5B9-168C-E611-A6E1-00266CFFBC60.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/ACC9B73F-648C-E611-BEC7-0242AC130005.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/ACEF7617-438C-E611-A591-0025904A8ECA.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/B609390C-1D8C-E611-BC76-0CC47A4C8E66.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/B81DB76B-608C-E611-9BD2-0025905A612C.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/C086DA91-FF87-E611-A751-008CFA064774.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/C0D91781-DA8C-E611-92C7-0CC47A0AD6AA.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/C4234B64-2B8C-E611-AB14-008CFA0A56F0.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/D256B9AB-2488-E611-9144-002618FDA287.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/EEAB2F70-608C-E611-BBE1-0025905A60AA.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/F0531604-DC8C-E611-A3E0-003048FFCBB8.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/FCDCD0E5-6E87-E611-8080-0025905A60C6.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/FE490343-118C-E611-89DD-003048322B62.root',
       '/store/data/Run2016B/SingleElectron/MINIAOD/23Sep2016-v2/80000/FE713B6A-6B8C-E611-B0F8-0025905B85DA.root',
] )
