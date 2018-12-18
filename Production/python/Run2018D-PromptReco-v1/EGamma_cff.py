import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v1/000/320/413/00000/EC137CAB-5593-E811-A61C-FA163ECE1720.root',
       '/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v1/000/320/416/00000/204B9A5B-5893-E811-AFE2-FA163E439461.root',
       '/store/data/Run2018D/EGamma/MINIAOD/PromptReco-v1/000/320/434/00000/1858FF04-BD93-E811-A4C8-FA163E472C72.root',
] )
