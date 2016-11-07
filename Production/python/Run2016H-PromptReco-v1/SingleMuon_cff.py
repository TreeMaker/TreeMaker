import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/085/00000/C2ABE862-897F-E611-9BB9-FA163E6734CA.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/090/00000/14840EE8-C27F-E611-B9E4-02163E011A1B.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/117/00000/1ED05AD2-0D80-E611-90C7-FA163E823565.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/130/00000/0A6659F4-7980-E611-ACAF-02163E014189.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/131/00000/C89845BF-9580-E611-B7BC-02163E01420B.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/145/00000/18AB2A0B-BC80-E611-A9C7-02163E0134FA.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/156/00000/8C157B9E-D180-E611-930B-02163E01264C.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/165/00000/2E0D0334-D480-E611-AA5C-02163E0143F6.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/166/00000/A07C8A75-D980-E611-982E-FA163E243E4B.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/167/00000/DA0DB2B3-E480-E611-9539-02163E01237C.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/178/00000/7AB31A37-F980-E611-83F1-FA163E193310.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/189/00000/BEB5F6BC-0A81-E611-AE0C-02163E014334.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/201/00000/94C7DC57-6A81-E611-B9C0-FA163ECAEAEF.root',
       '/store/data/Run2016H/SingleMuon/MINIAOD/PromptReco-v1/000/281/202/00000/264126FC-6B81-E611-94DA-FA163ED91A14.root',
] )
