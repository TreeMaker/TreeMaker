import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/604/00000/A2C8CC59-942A-E511-83C6-02163E012AB6.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/612/00000/7E50A9E3-9C2A-E511-9AC7-02163E0126E1.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/638/00000/182D8570-032B-E511-93BD-02163E0144D6.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/642/00000/0E3CD642-DB2A-E511-B72F-02163E012601.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/643/00000/7037210F-8D2C-E511-A430-02163E01340A.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/721/00000/2A828FCA-182C-E511-9AF1-02163E01299A.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/781/00000/A46B1D61-AE2C-E511-8AF1-02163E011D37.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/251/883/00000/AE652347-4A2D-E511-80E4-02163E013417.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/252/102/00000/2AB24187-DA2F-E511-9840-02163E0124CC.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/252/116/00000/6ECD6E96-7A30-E511-8F97-02163E011D0F.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/252/126/00000/64FBF8C7-E530-E511-81B6-02163E013406.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/252/488/00000/FCE41170-F335-E511-883D-02163E014544.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/252/496/00000/FA6746F4-CD35-E511-9612-02163E014241.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/252/499/00000/C08CE219-D135-E511-82E7-02163E0135D1.root',
       '/store/data/Run2015B/HTMHT/MINIAOD/PromptReco-v1/000/252/501/00000/56B629B6-CE35-E511-860D-02163E0145CD.root' ] );


secFiles.extend( [
               ] )

