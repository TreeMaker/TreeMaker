import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/100000/D2C4EF69-1DF0-E611-A419-0CC47A7D9966.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/1010000/D86BE570-F1EF-E611-8930-0CC47A7DFF52.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/1010000/E88DCD3C-F2EF-E611-96BB-0CC47A7DFF52.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/1010000/F607EC90-F2EF-E611-83D2-002590DB92A8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/110000/FCB854DA-55EC-E611-AF52-0CC47A7FC844.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/80000/14B8BC18-05EE-E611-9CD4-002590DB05F4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/80000/1883CE6B-CCED-E611-9619-0CC47A7E6A42.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/80000/1A062D42-12EE-E611-8B72-0025907DB9F8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/80000/66B37C3A-12EE-E611-8287-0CC47A7FC7B2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/80000/74412F5F-12EE-E611-B7A0-0CC47A7E6A3E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/80000/846E74A6-0CEE-E611-AA88-047D7BD6DE24.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/80000/A40ABE21-0EEE-E611-9447-0CC47A7FC736.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/03Feb2017_ver3-v1/80000/F892EBB2-2CEE-E611-9522-70106F4A96E8.root',
] )
