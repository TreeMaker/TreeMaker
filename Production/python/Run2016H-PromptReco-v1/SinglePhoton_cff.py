import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/085/00000/DEB65245-897F-E611-AC24-02163E01431B.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/090/00000/C08D69D7-C27F-E611-92A8-02163E014731.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/117/00000/9C5BEF6B-0D80-E611-8A7B-02163E014224.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/130/00000/F0A10D1D-7680-E611-883F-02163E0135DF.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/131/00000/4A8BADEC-9580-E611-A950-FA163E2B3AA9.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/145/00000/3A2AA865-BB80-E611-A76D-FA163E4CF297.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/156/00000/70A7FB4E-D080-E611-AB9F-FA163E3A12F2.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/165/00000/06A13E2D-D480-E611-AADA-FA163E4CF297.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/166/00000/E43BC9AB-D980-E611-B53C-02163E0119EE.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/167/00000/02B12C6A-E380-E611-9BAC-02163E01296C.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/178/00000/6237D1B5-F880-E611-B5AD-FA163E073540.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/189/00000/C8454B29-0A81-E611-A244-02163E012865.root',
       '/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v1/000/281/201/00000/62E21177-6981-E611-B50D-02163E01467F.root',
] )
