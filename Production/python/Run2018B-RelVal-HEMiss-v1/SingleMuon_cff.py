import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_sigMu2018B-v1/10000/647933DD-0180-E811-BCA6-0CC47A4D7650.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_sigMu2018B-v1/10000/66F6FE9C-ED7F-E811-B3A2-0CC47A7C361E.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_sigMu2018B-v1/10000/6A651288-EF7F-E811-9413-0025905B8598.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_sigMu2018B-v1/10000/98448AAA-E87F-E811-92C5-0CC47A4D75EE.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_sigMu2018B-v1/10000/B4786431-EC7F-E811-88B4-0025905B8586.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_sigMu2018B-v1/10000/C0164D15-0780-E811-8FE7-0CC47A4D76A0.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_sigMu2018B-v1/10000/C22BB9A2-EC7F-E811-9BF6-0025905A6082.root',
       '/store/relval/CMSSW_10_1_7/SingleMuon/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_sigMu2018B-v1/10000/F0173B54-EA7F-E811-A82E-003048FFCBB8.root',
] )
