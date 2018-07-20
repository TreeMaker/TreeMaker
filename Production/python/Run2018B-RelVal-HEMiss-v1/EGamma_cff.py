import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/00BCDF45-3680-E811-9772-0CC47A7C3638.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/02D7C7F6-3980-E811-97C6-0CC47A4C8E46.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/12DCC0C6-2E80-E811-96F3-0CC47A7C354C.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/221343B3-2D80-E811-96C5-0025905A60BE.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/38F222B6-1480-E811-8821-0025905A6068.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/86B9305D-3180-E811-A6A2-0CC47A4D769A.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/8A653230-3480-E811-A760-0CC47A4C8E56.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/C43E8D87-3280-E811-A730-0025905B856E.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/E4842E54-1880-E811-AFF9-0025905B85DE.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_HEmiss_v1_RelVal_EGamma2018B-v1/10000/FA2A30FE-5580-E811-81EA-0025905A48C0.root',
] )
