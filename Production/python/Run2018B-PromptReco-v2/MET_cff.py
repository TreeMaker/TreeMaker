import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/432/00000/480B3E71-9F78-E811-93C1-FA163EF1FB9C.root',
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/563/00000/7AFBAA29-ED79-E811-A233-FA163E03CDF2.root',
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/651/00000/0AD4A1ED-A07A-E811-BB2F-FA163EDD6A45.root',
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/733/00000/CC783399-9C7B-E811-BAE4-02163E01A068.root',
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/816/00000/10D788A7-A97C-E811-80CB-FA163E950A52.root',
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/827/00000/C8B2C390-2E7C-E811-9C27-FA163E7B6908.root',
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/828/00000/386573CE-787C-E811-B784-FA163E61E995.root',
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/828/00000/48E93B0B-767C-E811-846E-FA163E56D1F9.root',
       '/store/data/Run2018B/MET/MINIAOD/PromptReco-v2/000/318/856/00000/30951A47-597C-E811-A709-FA163EDD6108.root',
] )
