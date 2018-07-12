import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/MET/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_met2018B-v1/10000/90D00A29-DE7F-E811-AD17-0CC47A78A414.root',
       '/store/relval/CMSSW_10_1_7/MET/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_met2018B-v1/10000/B0DB8D12-DD7F-E811-B5AF-0CC47A78A456.root',
       '/store/relval/CMSSW_10_1_7/MET/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_met2018B-v1/10000/E683DC2C-E17F-E811-A689-0CC47A4D766C.root',
] )
