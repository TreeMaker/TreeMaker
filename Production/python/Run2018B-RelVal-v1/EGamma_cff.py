import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/169FB560-2E80-E811-BB39-0CC47A7C360E.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/32E66EF5-2780-E811-8696-0CC47A4D7614.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/40F2FCB8-5280-E811-9FED-0CC47A7C340C.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/50A16101-4680-E811-8749-0CC47A7C3424.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/62D1024D-4E80-E811-85D3-0025905A610A.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/906C4C35-2B80-E811-BD75-0CC47A4D7654.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/A6FF79D1-3580-E811-B3B5-0CC47A78A458.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/CAD0DC45-2D80-E811-93D4-0025905A6094.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/CAD875E2-3080-E811-87E0-0CC47A78A3EC.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/D07AD96F-2980-E811-A24E-0CC47A7C3412.root',
       '/store/relval/CMSSW_10_1_7/EGamma/MINIAOD/101X_dataRun2_Prompt_v11_RelVal_EGamma2018B-v1/10000/E82B91AB-4980-E811-AA7E-0CC47A4C8F2C.root',
] )
