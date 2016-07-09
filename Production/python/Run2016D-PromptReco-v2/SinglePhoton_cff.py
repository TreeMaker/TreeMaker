import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/315/00000/04274087-F944-E611-9018-02163E01457A.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/315/00000/2E9B5790-F944-E611-BFC5-02163E0133DD.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/315/00000/461D4991-F944-E611-8DA5-02163E01374F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/315/00000/4ABB2699-F944-E611-9218-02163E0144A4.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/315/00000/BE3238AB-F944-E611-AD05-02163E014259.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/317/00000/4273AED9-1745-E611-B797-02163E01466B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/317/00000/585BECAF-1945-E611-8D75-02163E0119BF.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/317/00000/A2220860-1445-E611-8071-02163E01442E.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/317/00000/DE9EC1AE-1745-E611-AF8F-02163E014413.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/180E6ADB-2545-E611-98F1-02163E013950.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/1CA0F145-2545-E611-B4A6-02163E012598.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/2CEC3BEA-2545-E611-9E16-02163E012ABC.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/48528AA2-2445-E611-AAAB-02163E011888.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/4E76633E-2645-E611-8121-02163E0144AC.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/68FD6D51-2645-E611-AFAD-02163E011FCE.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/76C1E5E4-2545-E611-BA63-02163E0137F8.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/B46FCD51-2645-E611-A970-02163E01468B.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/CE026102-2645-E611-A5F5-02163E0143F9.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/D2A32996-2445-E611-AF89-02163E014517.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/F0653CA8-2445-E611-9AF0-02163E014539.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/318/00000/F69F6D96-2445-E611-BFCE-02163E01186F.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/327/00000/10BF1C0E-5145-E611-9789-02163E012B5D.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/327/00000/42A755E8-5045-E611-B32D-02163E0134C9.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/347/00000/AC907FBB-5545-E611-8F44-02163E013430.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/352/00000/4CB4B8D9-5845-E611-904C-02163E014536.root',
       '/store/data/Run2016D/SinglePhoton/MINIAOD/PromptReco-v2/000/276/352/00000/B6960DFC-5845-E611-855E-02163E0142ED.root',
] )
