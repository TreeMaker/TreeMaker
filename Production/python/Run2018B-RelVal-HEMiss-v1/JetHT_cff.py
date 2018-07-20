import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_jetHT2018B-v1/10000/00DBB9B1-1280-E811-A08D-0025905B85BC.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_jetHT2018B-v1/10000/0453F57F-1480-E811-9B22-0CC47A4C8F12.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_jetHT2018B-v1/10000/32AC5D94-1080-E811-A11D-0CC47A4C8F12.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_jetHT2018B-v1/10000/3C8CA11A-0280-E811-810C-0025905A60F4.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_jetHT2018B-v1/10000/84880955-1680-E811-9CE8-0025905A60A8.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_jetHT2018B-v1/10000/A61DE4BE-0B80-E811-B433-0CC47A7C3404.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_jetHT2018B-v1/10000/F025E36F-1D80-E811-967D-0CC47A4D75EC.root',
       '/store/relval/CMSSW_10_1_7/JetHT/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_jetHT2018B-v1/10000/F8921004-1980-E811-9FDC-0CC47A4D76D6.root',
] )
