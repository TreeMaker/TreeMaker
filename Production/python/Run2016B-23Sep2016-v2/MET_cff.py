import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/10FC1547-B184-E611-960D-141877640173.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/3A694282-B284-E611-B060-901B0E5427B6.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/3C95F5D7-DA84-E611-B141-001E0BC198D8.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/422FC4A3-8685-E611-B6FF-B083FED04276.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/50612202-8E86-E611-B9D1-002590207984.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/50F46233-F885-E611-BCF5-0022195E678D.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/686E2C00-8E86-E611-83F6-0CC47ABB5178.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/7C7BB40A-8685-E611-9A65-0CC47A1E0DCA.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/7EB54339-3285-E611-95BD-20CF3027A592.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/8E6F6DE3-CB84-E611-956E-001E67581494.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/903299FC-8D86-E611-9428-44A84223FF3C.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/BA93A59B-B384-E611-BD68-00259073E492.root',
       '/store/data/Run2016B/MET/MINIAOD/23Sep2016-v2/70000/FA27F0FF-8D86-E611-866C-001A648F1DFA.root',
] )
