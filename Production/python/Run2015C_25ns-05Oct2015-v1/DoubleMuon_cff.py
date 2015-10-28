import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/0811243A-6E74-E511-9A9E-0025905A60B2.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/125039EF-7874-E511-95EB-0025905A60E4.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/2A7D15F1-7874-E511-B57D-0025905A48C0.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/2E8D522D-6E74-E511-BE86-0025905A48D0.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/347E5298-7074-E511-998F-0025905A611C.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/3C8FDAC6-AA74-E511-9A5D-0025905B859E.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/5066BCB7-7474-E511-A083-0025905B85D8.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/5AC18B3E-6E74-E511-9E15-0025905A60BC.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/6260220F-6074-E511-AE86-0025905A609E.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/6CE8C281-6A74-E511-8EDC-0025905964CC.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/6EEBF8CF-7274-E511-9538-002618943918.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/762C3383-7D74-E511-A5FC-00261894390A.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/A0BF9B17-5F74-E511-83B8-0025905A48C0.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/AC9E2C97-6874-E511-B08C-0025905A60A8.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/BA04450C-6C74-E511-B5E1-0025905A60F2.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/C6B15E1D-7974-E511-87BE-0025905B85B2.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/C8DB1F45-6E74-E511-B0ED-002590593872.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/D4286434-5F74-E511-87D6-0025905A60B4.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/DE21EC21-6E74-E511-84B5-002618943918.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/E699EABF-6F74-E511-9A5C-0025905A6110.root',
       '/store/data/Run2015C_25ns/DoubleMuon/MINIAOD/05Oct2015-v1/50000/E6CE490C-6C74-E511-B175-0025905B858A.root' ] );


secFiles.extend( [
               ] )

