import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/14F2C765-2580-E811-9D1B-0CC47A4D7690.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/3A5A4365-3F80-E811-80B2-0025905B8586.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/440F783F-2180-E811-9F5D-0025905B8594.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/4C6C06E5-3C80-E811-B278-0025905A6094.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/503DB507-2380-E811-AF85-0CC47A7C3410.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/7C654EDD-3780-E811-903D-0025905B8604.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/86E888D7-3480-E811-BC5F-0CC47A4D761A.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/A20C0E46-1F80-E811-BA58-0025905B8586.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_sigMu2018B-v1/10000/AE796163-8A80-E811-A6D6-0025905B8598.root',
] )
