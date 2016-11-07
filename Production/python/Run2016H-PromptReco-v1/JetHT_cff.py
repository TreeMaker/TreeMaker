import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/010/00000/2CEFC128-757E-E611-A6CB-02163E014679.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/085/00000/7E4416FF-887F-E611-9882-02163E0134A5.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/090/00000/CE81D20C-C37F-E611-ADA9-02163E01431B.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/117/00000/5CACF77F-0D80-E611-9F04-02163E01430B.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/130/00000/A4836AAA-7880-E611-9974-02163E01472A.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/131/00000/3AEDC011-9D80-E611-915C-FA163EDE598F.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/145/00000/38B8A77F-BB80-E611-8A23-02163E013579.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/156/00000/F4E4C8A6-D080-E611-95E8-FA163E8C4370.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/165/00000/8C355254-D480-E611-BAF0-02163E0145B2.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/166/00000/CC52562E-DA80-E611-B5F0-FA163E720510.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/167/00000/C29ED806-E380-E611-B40C-FA163E4FF519.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/178/00000/8E2B831A-F980-E611-9270-02163E011AEE.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/189/00000/12C2DA56-0981-E611-88BE-FA163E298B60.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/201/00000/AC5F9427-6A81-E611-A899-02163E01420B.root',
       '/store/data/Run2016H/JetHT/MINIAOD/PromptReco-v1/000/281/202/00000/20E08234-6B81-E611-A504-FA163E60DE95.root',
] )
