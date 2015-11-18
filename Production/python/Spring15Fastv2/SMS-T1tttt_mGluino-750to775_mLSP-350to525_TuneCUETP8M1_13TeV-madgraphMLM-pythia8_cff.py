import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/062917BC-1E7F-E511-9521-02163E013E50.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0847F297-1F7F-E511-8C9C-02163E011544.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0CF628B9-1E7F-E511-93AE-02163E0115E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1AABA3EE-1E7F-E511-A2AB-02163E013EC4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1ABB07D5-1E7F-E511-99D4-02163E0153A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1EF100CF-1E7F-E511-8CE8-02163E0114DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/20B5B0BD-1E7F-E511-82D4-02163E0147AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2224AEBD-1E7F-E511-BB84-02163E011458.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2EC99F2E-1F7F-E511-9C4B-02163E0152CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4029E9BE-1E7F-E511-ACBC-02163E01525F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/404EE2C3-1E7F-E511-BFD7-02163E014E96.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/42AB64C3-1F7F-E511-B718-02163E012D5F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/483E92B2-1E7F-E511-996D-0025905A60F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4CCDBEC5-1E7F-E511-BC8A-02163E016B4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/50199F44-1F7F-E511-B388-02163E010C7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/581F6EB8-1E7F-E511-BF5F-0025905B8572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5A2F45B1-1E7F-E511-9162-0025905A60EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5A4478B9-1E7F-E511-95C1-02163E0115E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/662D3EB3-1E7F-E511-BD1A-008CFA197D2C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6C8212C0-1E7F-E511-86B1-02163E0115F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6C93435F-1F7F-E511-8DA6-02163E0114A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/70DC5AE9-217F-E511-806A-02163E011553.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/76619BC1-1E7F-E511-AB34-02163E0131F9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7C8EF5CA-1E7F-E511-A6BB-02163E0148DE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8C8CCF2D-1F7F-E511-A499-02163E0117C2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8CBBD5EE-1E7F-E511-B345-02163E013EC4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/942494FA-1F7F-E511-9BD9-02163E0114CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/98518443-1F7F-E511-B305-02163E00C8BD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A078D2BC-1E7F-E511-9B4E-02163E011458.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B4EFB2B9-1F7F-E511-A07F-02163E0114D3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B8A8FBBE-1E7F-E511-B764-02163E01525F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C2C2CABC-1E7F-E511-9BF0-02163E016BB2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C4583DDA-1E7F-E511-97B2-02163E010E69.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C8C64370-1F7F-E511-A89C-02163E00F3AB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CECDE042-207F-E511-B20D-02163E0114CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D2E18CAD-1E7F-E511-A8AF-90B11C08AD7D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DC988CB0-1E7F-E511-9D81-002618943807.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DE5C5CCA-1E7F-E511-8889-02163E015033.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DECF63FA-1E7F-E511-BB83-02163E014D07.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EE6C3CD4-1E7F-E511-9706-02163E0116D3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-750to775_mLSP-350to525_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F47732C8-1E7F-E511-B931-0025905A60CA.root' ] );


secFiles.extend( [
               ] )

