import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/010/00000/8EC4E0C4-737E-E611-A807-FA163EE1D7FD.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/085/00000/D67B6615-897F-E611-BAA6-FA163ECD93DC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/090/00000/28C237D3-C57F-E611-BEBD-02163E0146BE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/117/00000/6EDE6211-0E80-E611-A569-FA163E4217D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/130/00000/4269171B-7880-E611-B021-FA163E21E657.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/131/00000/BAA79CC1-9580-E611-A92C-02163E01470F.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/145/00000/2A1869A8-BB80-E611-A3F0-FA163E6CB3A1.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/156/00000/52D2A0EC-D080-E611-9E6D-FA163ED91A14.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/165/00000/AC641745-D480-E611-A330-02163E0143DE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/166/00000/5821EE0E-DA80-E611-9346-FA163EEEC605.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/167/00000/209F357C-E480-E611-9619-02163E0146CC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/178/00000/140677F9-F780-E611-AD37-02163E014242.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/189/00000/F657659D-0981-E611-83D9-02163E014135.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/201/00000/A6A84D58-6A81-E611-8E92-FA163EA66D42.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/PromptReco-v1/000/281/202/00000/6A9C69BA-6B81-E611-A04E-02163E01347D.root',
] )
