import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/315/00000/262E7B46-F444-E611-8652-02163E011FD5.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/315/00000/7EFCEE5B-F444-E611-AC64-02163E0124FC.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/315/00000/EE3B604A-F444-E611-9BEF-02163E014704.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/317/00000/3AEC63BC-0445-E611-B4D7-02163E012B5D.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/317/00000/80672480-0545-E611-813D-02163E014137.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/317/00000/F06CE88C-0545-E611-A7FC-02163E0141DD.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/2AC09EC9-3445-E611-B2DE-02163E0123C6.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/54FF0BAD-3445-E611-A07E-02163E011C6A.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/62D9F396-3445-E611-88E9-02163E0133E2.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/86CF63CB-3445-E611-AA6F-02163E013749.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/A2245DA2-3445-E611-9404-02163E0142D1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/A48F58B2-3445-E611-89CC-02163E01187B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/318/00000/EA648EB6-3445-E611-9120-02163E011C7B.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/327/00000/98E89C1D-5145-E611-8335-02163E0145A1.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/347/00000/227F032A-5445-E611-8627-02163E013873.root',
       '/store/data/Run2016D/MET/MINIAOD/PromptReco-v2/000/276/352/00000/3C983FB1-5845-E611-AFBC-02163E01365B.root',
] )
