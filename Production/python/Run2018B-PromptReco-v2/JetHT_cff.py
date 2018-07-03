import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/432/00000/60A884F2-9F78-E811-B7E7-FA163E6967EB.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/563/00000/90DCC2ED-EC79-E811-896D-FA163EFDE902.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/651/00000/E883501A-A17A-E811-8248-FA163E10052D.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/733/00000/00D6C6D9-AA7B-E811-BF3A-02163E014B6E.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/827/00000/FAC8C177-2E7C-E811-8CC6-FA163E7B6908.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/828/00000/1862136C-7C7C-E811-A337-FA163E5DF416.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/828/00000/98ABD2DD-727C-E811-B34E-FA163E7CFF74.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/828/00000/BCFE16ED-667C-E811-AA08-02163E00AF4E.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/828/00000/D67B05D4-6D7C-E811-BB46-FA163E7219FB.root',
       '/store/data/Run2018B/JetHT/MINIAOD/PromptReco-v2/000/318/856/00000/6211C9F9-587C-E811-8DA4-FA163E6446D4.root',
] )
