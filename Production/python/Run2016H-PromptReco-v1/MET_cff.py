import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/010/00000/3EC068A9-747E-E611-BC5F-02163E014488.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/085/00000/786DC329-897F-E611-A7DD-02163E011BA2.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/090/00000/6C9F3EE0-C27F-E611-93CA-02163E01419A.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/117/00000/2815332E-0D80-E611-B50F-FA163ECAAE3F.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/130/00000/B8E7A92B-7780-E611-85EC-02163E014195.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/131/00000/0AE4E4A5-9680-E611-9DA3-FA163EE27131.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/145/00000/96001C2D-BC80-E611-A5A0-02163E0142C4.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/156/00000/82599EF1-D080-E611-944D-02163E014748.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/165/00000/FAE07841-D480-E611-8AE7-02163E0145EF.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/166/00000/00DC5909-DA80-E611-9DB7-02163E01463B.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/167/00000/34376E75-E380-E611-BE55-02163E01433A.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/178/00000/8CE49D78-FB80-E611-B231-FA163EF5C1F9.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/189/00000/5ED95781-0881-E611-BFED-FA163ECD47C3.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/201/00000/E65E4FD1-6C81-E611-B5EA-02163E014775.root',
       '/store/data/Run2016H/MET/MINIAOD/PromptReco-v1/000/281/202/00000/4874094C-6B81-E611-A6A4-02163E014708.root',
] )
