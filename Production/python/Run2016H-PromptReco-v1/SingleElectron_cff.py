import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/085/00000/D61ED559-887F-E611-8939-FA163E99558E.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/090/00000/A4F7EA80-C27F-E611-9442-02163E013992.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/117/00000/AABF3E3C-0D80-E611-9205-02163E01410E.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/130/00000/B6508C23-7780-E611-98BC-02163E013670.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/131/00000/FE28E855-9680-E611-A79C-FA163E11C6A3.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/145/00000/A04F81D3-BB80-E611-AF86-FA163E5942E4.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/156/00000/0E2384AC-D080-E611-9978-02163E014748.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/165/00000/E8F00F48-D480-E611-85F4-02163E011D0A.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/166/00000/FACA9B33-DA80-E611-B448-02163E01418C.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/167/00000/1C42FFD8-E280-E611-ABAC-FA163EDE598F.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/178/00000/C0155CC7-F780-E611-ADE4-FA163E4FF519.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/189/00000/002EEDE5-0881-E611-89C7-FA163E5B1EE0.root',
       '/store/data/Run2016H/SingleElectron/MINIAOD/PromptReco-v1/000/281/201/00000/E46B086B-6981-E611-BA57-FA163EE5CB53.root',
] )
