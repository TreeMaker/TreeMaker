import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/251/604/00000/BC1ACF99-902A-E511-8388-02163E012183.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/251/612/00000/D83A3D7C-952A-E511-A5A3-02163E012603.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/251/638/00000/D25E02F6-412B-E511-9652-02163E011861.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/251/642/00000/B209CE06-D62A-E511-8FCE-02163E014637.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/251/643/00000/CC77B94F-902C-E511-9A26-02163E01369B.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/251/721/00000/DA65D5C2-142C-E511-B28E-02163E0134B7.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/251/781/00000/D857250B-A02C-E511-A43C-02163E0136E2.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/251/883/00000/E070C347-492D-E511-8D03-02163E011E24.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/252/102/00000/180A5A92-DA2F-E511-90E7-02163E0124CC.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/252/116/00000/1A26DF89-4E30-E511-8787-02163E0135B4.root',
       '/store/data/Run2015B/MET/MINIAOD/PromptReco-v1/000/252/126/00000/428F4483-C730-E511-B77E-02163E012620.root'
       ] );


secFiles.extend( [
               ] )
