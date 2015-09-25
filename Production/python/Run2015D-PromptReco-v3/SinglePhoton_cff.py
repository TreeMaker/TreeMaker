import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/584/00000/AE89EEAF-855D-E511-9B3B-02163E013592.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/587/00000/9281243A-945D-E511-96EF-02163E011FBB.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/629/00000/3C869B3B-115F-E511-AB40-02163E0146D2.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/630/00000/BE4748B0-295F-E511-A271-02163E014402.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/662/00000/A24157CC-075F-E511-89E9-02163E013458.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/672/00000/E4C5C3DF-025F-E511-997E-02163E013918.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/673/00000/7C000AF7-225F-E511-BE0C-02163E0145CB.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/674/00000/E253BB08-065F-E511-8CD9-02163E011BE4.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/675/00000/6EA59418-B25F-E511-A0E7-02163E01371D.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/675/00000/DEEB4718-B25F-E511-914A-02163E011A8A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/0A062686-AC5F-E511-84C8-02163E011FAC.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/42BA7A81-AC5F-E511-B616-02163E011A8A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/48A7748A-AC5F-E511-AF81-02163E0144C7.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/48E36F80-AC5F-E511-B938-02163E0143E2.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/66CA398E-AC5F-E511-A0A3-02163E01431C.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/A404177F-AC5F-E511-9753-02163E013411.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/676/00000/DCFF7489-AC5F-E511-88F8-02163E01393E.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/677/00000/4031592C-275F-E511-9187-02163E0141D6.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/677/00000/80F90E1E-275F-E511-831C-02163E01474F.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/677/00000/D0AEFD42-275F-E511-B80B-02163E01443C.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/721/00000/D89CF3C6-075F-E511-9810-02163E014504.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/725/00000/040FBC97-395F-E511-9CA8-02163E0136E3.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/727/00000/4884FAD6-435F-E511-9476-02163E0144BA.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/728/00000/8C18777C-3A5F-E511-BD8C-02163E013390.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/12C1D1E8-3E60-E511-981E-02163E011C91.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/2A6652EC-3E60-E511-8619-02163E014734.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/2C16C805-3F60-E511-A4C5-02163E012096.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/44331506-3F60-E511-8DE2-02163E01475F.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/482403E7-3E60-E511-BCA2-02163E011FEF.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/7699BEE7-3E60-E511-9D68-02163E0139E0.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/84144104-3F60-E511-97DF-02163E012A7D.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/920AD7EC-3E60-E511-A5DA-02163E012434.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/729/00000/DE0B41EA-3E60-E511-ADC6-02163E01352A.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/734/00000/DA6FF6AD-E85F-E511-A08B-02163E012753.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/734/00000/E28307AE-E85F-E511-8AC6-02163E01210D.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/798/00000/7245B4EB-B15F-E511-91C0-02163E0128A8.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/801/00000/308FD73F-7860-E511-A85C-02163E011B36.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/801/00000/38C6B036-7860-E511-811B-02163E01463F.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/834/00000/DCD553A3-0060-E511-A6F1-02163E011A43.root',
       '/store/data/Run2015D/SinglePhoton/MINIAOD/PromptReco-v3/000/256/842/00000/C6A64E67-6360-E511-83B9-02163E014792.root' ] );


secFiles.extend( [
               ] )

