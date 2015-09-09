import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/604/00000/AE22AF42-902A-E511-8A22-02163E012B30.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/612/00000/50DA7894-932A-E511-801E-02163E0136A2.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/628/00000/40EF63A0-B52A-E511-8B57-02163E0133F0.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/638/00000/0CDDB666-E72A-E511-9BFD-02163E011DE5.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/638/00000/B2FC1038-372B-E511-AA94-02163E013481.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/642/00000/2C622272-D02A-E511-9F20-02163E013645.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/0E4B7E28-8D2C-E511-BFDA-02163E01477B.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/1247CF12-932C-E511-B9ED-02163E01354D.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/3A437BCB-912C-E511-96D0-02163E012934.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/7077210E-8F2C-E511-97D5-02163E0138EC.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/9EFCB7EB-C12C-E511-B8BB-02163E012158.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/A42F5B12-9C2C-E511-AAB3-02163E0134C3.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/C2E62796-942C-E511-8869-02163E0121A1.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/CCA6600A-912C-E511-B1EF-02163E0133D0.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/643/00000/D84DA8FC-8F2C-E511-9B5A-02163E01420D.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/716/00000/02C46BE4-302C-E511-A01C-02163E0128BF.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/721/00000/9663EE89-022C-E511-985A-02163E01359E.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/721/00000/CADC920F-E02B-E511-BB9B-02163E01412F.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/781/00000/662647FF-9B2C-E511-85C5-02163E012965.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/00CD59FD-2B2D-E511-8DB2-02163E01267F.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/500D754A-292D-E511-AEBA-02163E0118F2.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/CA2F0F5F-242D-E511-96AB-02163E011D88.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/CAA3B776-312D-E511-923A-02163E01280D.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/251/883/00000/D030EA86-9C2D-E511-8FCB-02163E014181.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/102/00000/06E11C1F-DA2F-E511-B04A-02163E0117FF.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/116/00000/2EE8BBD0-7730-E511-95F5-02163E013560.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/126/00000/7E4ACB62-6E31-E511-858C-02163E0133F0.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/126/00000/AA0C0594-CA30-E511-BD15-02163E0123C0.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/488/00000/B4D62F1C-EE35-E511-BAFE-02163E01477B.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/489/00000/686DE8AC-3334-E511-BAF8-02163E0144F6.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/490/00000/E2682AAA-3334-E511-9706-02163E012B10.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/492/00000/16665670-4734-E511-9940-02163E013901.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/496/00000/2CA28248-CC35-E511-BB41-02163E01258B.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/499/00000/DC5562FB-CB35-E511-99EB-02163E0125D6.root',
       '/store/data/Run2015B/SingleElectron/MINIAOD/PromptReco-v1/000/252/501/00000/A27F94C6-CA35-E511-82EC-02163E01459D.root' ] );


secFiles.extend( [
               ] )

