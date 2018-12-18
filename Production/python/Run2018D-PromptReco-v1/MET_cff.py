import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018D/MET/MINIAOD/PromptReco-v1/000/320/413/00000/3C7AF665-5693-E811-AAA6-FA163ECE1720.root',
       '/store/data/Run2018D/MET/MINIAOD/PromptReco-v1/000/320/416/00000/C43408EC-5893-E811-AE86-FA163E9CD516.root',
       '/store/data/Run2018D/MET/MINIAOD/PromptReco-v1/000/320/434/00000/748A99F9-BD93-E811-87D4-FA163E591793.root',
] )
