import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_jetHT2018B-v1/10000/186E3EB8-1D80-E811-81CB-0CC47A4C8F0A.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_jetHT2018B-v1/10000/187CE572-2180-E811-BA3E-0CC47A7C3638.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_jetHT2018B-v1/10000/2C2FEA2C-0F80-E811-8AAD-0025905A60DE.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_jetHT2018B-v1/10000/7AF671E2-2580-E811-8F4A-0025905B8594.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_jetHT2018B-v1/10000/82B0A9B3-2380-E811-80A8-0CC47A4D7628.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_jetHT2018B-v1/10000/ECCF7746-1180-E811-8816-0CC47A4C8F30.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_jetHT2018B-v1/10000/FC324170-5F80-E811-A3EA-0025905A60F8.root',
] )
