import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/0040ECBB-76EA-E611-8FE7-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/16F28614-84EA-E611-8083-A0369F310374.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/26C54321-7DEA-E611-97EC-B8CA3A70A5E8.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/36F116DC-8AEA-E611-84D5-24BE05C62711.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/40222852-7DEA-E611-9290-A0369F310374.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/42282F9B-75EA-E611-A0D2-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/4C3A6DE3-7DEA-E611-8664-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/520C6456-7DEA-E611-B733-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/52C02EA9-7EEA-E611-BA67-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/62689638-84EA-E611-BD20-B8CA3A70BAC8.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/70A3D0A6-7EEA-E611-BD71-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/7C6611B8-76EA-E611-8644-24BE05C636E1.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/88639E52-7DEA-E611-9102-A0369F310374.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/88EECBB2-91EA-E611-8C21-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/9620E3D8-7DEA-E611-BF13-24BE05C6E7C1.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/9C332DDA-7DEA-E611-8821-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/A606F1A0-75EA-E611-814B-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/AAE018B8-76EA-E611-A676-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/AAE662B8-76EA-E611-811A-5065F381A2F1.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/B4FAEA51-7DEA-E611-9BB6-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/B80050BC-76EA-E611-B0B0-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/BAAAA854-84EA-E611-9A52-B8CA3A70BAC8.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/C04E3FBD-76EA-E611-AA2F-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/C6CF8076-8BEA-E611-94E0-24BE05CE3C91.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/CE0D2338-7DEA-E611-A8F7-A0369F310374.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/CE40C7B7-76EA-E611-BD9F-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/DC5FA286-7CEA-E611-982C-B8CA3A70A5E8.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/E2FBF0A1-84EA-E611-8A3F-002590D9D9F0.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/F001FEB6-76EA-E611-A1C3-A0000420FE80.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver3-v1/80000/F0B09550-7DEA-E611-A445-B8CA3A70A5E8.root',
] )
