import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/08AD38C0-6C80-E511-9531-008CFA165FD0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0AAF65D6-5280-E511-9FDF-02163E010DED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/129C3D0F-7580-E511-A0EB-008CFA1CB55C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/12F0A48D-5480-E511-94E8-008CFA1C64B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/18364F90-5680-E511-9428-02163E00F78B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C5AE35A-6B80-E511-AC12-008CFA0A58B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C9E8BD8-6080-E511-ABF6-008CFA1CB55C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/20D563B8-9080-E511-A676-02163E00F37E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/26925AB2-6980-E511-BAE2-008CFA05EA18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/2EC5B065-5780-E511-BD4A-02163E00EA1B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/347C8ECE-6780-E511-A8BF-A0369F7FE970.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/401E477D-A780-E511-9F91-782BCB2058AD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/40B6AFC1-6C80-E511-B51C-008CFA1CB55C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/42235628-6E80-E511-B8F0-008CFA0A571C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/42500810-7580-E511-A3E8-008CFA1982C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/42608506-5B80-E511-B9FF-02163E010DB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/46FB5CEC-8A80-E511-90DB-008CFA14F814.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4C8C80D6-9080-E511-96E4-02163E016BE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/50C7E091-5480-E511-AF05-549F35AC7DEE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5C9F1579-9080-E511-92A8-02163E016B7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/66274BC1-6C80-E511-A338-008CFA1C6448.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6A4CE55C-6380-E511-9BEC-008CFA05EA2C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6AFAD194-9080-E511-9BB8-02163E0152E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/72B20358-6380-E511-BC37-549F35AF4461.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7C04BF94-B480-E511-84EB-02163E010FED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/847113D9-8D80-E511-B641-008CFA0A5808.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8494B8D2-5880-E511-B8D7-02163E00F4D3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8CAB01CA-5880-E511-808A-02163E00F4C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B00386CB-6580-E511-A0F4-008CFA05E8EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B44BB8CA-6580-E511-BF9F-008CFA0A5614.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B4DB98D5-6780-E511-9CC3-008CFA064700.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BE9EA758-5980-E511-98C1-008CFA165FD0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C235F4C1-6C80-E511-8C1F-008CFA151F98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D0CE108D-9280-E511-87FF-02163E01680C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D62ED12D-5880-E511-81F4-02163E016BC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D6EF37EC-8A80-E511-977F-008CFA198258.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DC288154-5980-E511-A451-008CFA580730.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DE6F6B94-9080-E511-9815-02163E00F310.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DE841214-9180-E511-A2AE-02163E0167E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/E6841B6D-9080-E511-AAC2-001E67578FA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/EA22CC97-9080-E511-AB8C-02163E013F88.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F88291B3-6980-E511-B917-008CFA05EA24.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200to1225_mLSP-800to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F8EFF127-6E80-E511-859E-008CFA05E8EC.root' ] );


secFiles.extend( [
               ] )

