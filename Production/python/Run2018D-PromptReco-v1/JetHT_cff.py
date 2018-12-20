import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018D/JetHT/MINIAOD/PromptReco-v1/000/320/413/00000/B687B1C4-5593-E811-B393-FA163E8F4E24.root',
       '/store/data/Run2018D/JetHT/MINIAOD/PromptReco-v1/000/320/416/00000/B0AE3274-5993-E811-AD0A-02163E019F29.root',
       '/store/data/Run2018D/JetHT/MINIAOD/PromptReco-v1/000/320/434/00000/AA056E56-BD93-E811-99AC-02163E00CE99.root',
] )
