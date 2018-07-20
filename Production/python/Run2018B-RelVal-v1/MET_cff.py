import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/MET/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_met2018B-v1/10000/1E6B0659-F37F-E811-BACA-0025905A607A.root',
       '/store/relval/CMSSW_10_1_7/MET/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_met2018B-v1/10000/56D75E37-F07F-E811-B90C-0CC47A74524E.root',
       '/store/relval/CMSSW_10_1_7/MET/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_met2018B-v1/10000/BE4AFD69-EE7F-E811-B6EF-00248C55CC3C.root',
] )
