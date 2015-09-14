import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/604/00000/D02F3FAD-932A-E511-8196-02163E012B30.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/612/00000/B0976CB6-A12A-E511-BEE5-02163E012601.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/628/00000/901BCAD1-B52A-E511-99B0-02163E0146D1.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/638/00000/BEB8ACAE-F82A-E511-A5CB-02163E013793.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/642/00000/6C9BEE18-DA2A-E511-A902-02163E0133FF.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/643/00000/62942F94-912C-E511-80E0-02163E01340A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/643/00000/F05E88C1-762C-E511-B786-02163E011B6C.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/716/00000/FEEE8ED5-C32B-E511-9562-02163E013728.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/721/00000/CA2AB92F-192C-E511-B266-02163E011DCE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/781/00000/E6B7BCB8-B02C-E511-ADF5-02163E011D30.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/251/883/00000/DA459E92-4F2D-E511-AF66-02163E01474A.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/102/00000/743C3E35-D92F-E511-810C-02163E0139B0.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/116/00000/10293DB4-7730-E511-82D6-02163E0117FF.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/126/00000/DA16B12A-E930-E511-8AD3-02163E011A02.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/488/00000/608BCCA0-EE35-E511-BCDC-02163E0133D0.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/489/00000/E0CBB19E-3334-E511-817B-02163E0129DA.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/490/00000/14ADE2E4-3334-E511-888A-02163E014241.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/492/00000/2A8916FC-4634-E511-ADE6-02163E011DCE.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/496/00000/5E84A765-CB35-E511-B0C9-02163E0128F2.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/499/00000/687CE3FE-CB35-E511-9D42-02163E0143C9.root',
       '/store/data/Run2015B/DoubleEG/MINIAOD/PromptReco-v1/000/252/501/00000/B2B0FDD0-CA35-E511-BC25-02163E0138EC.root' ] );


secFiles.extend( [
               ] )

