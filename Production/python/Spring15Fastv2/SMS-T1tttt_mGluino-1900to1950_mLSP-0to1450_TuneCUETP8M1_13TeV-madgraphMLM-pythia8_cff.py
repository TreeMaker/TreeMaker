import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/043CE376-7383-E511-B2FF-008CFA056400.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0806B129-6B83-E511-B9BC-549F35AD8C0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1883D50B-BE83-E511-8DFB-008CFA05E898.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/18E368C9-5383-E511-AFB1-0CC47A009258.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1EBF1B24-6483-E511-B30F-782BCB1612C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/222866B0-B683-E511-8425-001EC9B21826.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/248D2DA6-8883-E511-BA6A-549F35AD8BC9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/24F2A6AE-8883-E511-9FC8-008CFA1979A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2CD6EFF6-5683-E511-B9CC-001EC9B1D3BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3027C185-B484-E511-A2A0-0025901AEC94.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/36B489B5-B683-E511-A929-0CC47A009E22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/38AB8D35-4983-E511-A471-FA163EBE6194.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/38BB5E04-4E83-E511-B8B8-FA163EFF5FD3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4427932D-6483-E511-9C6D-001EC9B21808.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4631972A-6B83-E511-8E63-549F358EB721.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4810A05A-B484-E511-81B2-02163E010ECF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48A29460-B484-E511-9985-02163E010EC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48D9DEF7-5683-E511-A6FC-0CC47A00A832.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C8A589B-7083-E511-8439-008CFA0516BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/50D7B029-6B83-E511-8080-549F35AD8C0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/560F86A3-8883-E511-A264-A0369F7FC070.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/56527728-6B83-E511-A0E3-549F358EB7BD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5A8C42EE-8783-E511-A17B-A0369F7F9EDC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/60BD312B-6B83-E511-BD5F-549F358EB76F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/629F16E7-C283-E511-A084-008CFA05EA18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66975F72-C083-E511-841E-008CFA05E898.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6A425C9E-8E83-E511-915E-A0369F7F9EDC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/76ABE72A-6B83-E511-BD50-00266CFCCB44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7A7BCF1B-8C83-E511-8317-549F35AC7E7D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E633495-4E83-E511-91E1-02163E0153D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/808116BF-5E83-E511-B818-549F35AD8BC9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/845E2D3A-8783-E511-B3CB-008CFA197A70.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/869E8D35-4983-E511-831C-FA163EBE6194.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8833804A-8783-E511-8F7B-A0369F7FC608.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8CA0BDC3-5083-E511-A6CE-FA163EB67116.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/92347642-B084-E511-8B91-02163E010DED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6A58B2B-8383-E511-B3BD-008CFA01E258.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AAC7352B-6383-E511-9257-549F358EB7B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AAC9D795-7783-E511-9B32-A0369F7FC544.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8CF4E2B-6B83-E511-BD0A-549F35AD8BE3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC439F68-B484-E511-9617-02163E013DBC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC53D9AF-8883-E511-B46E-549F35AE4FC9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BCA4B9F2-7D83-E511-9411-008CFA0A5A94.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BE8B05D7-4183-E511-ACBB-0CC47A009E22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2EBE7C2-5083-E511-B266-02163E0153D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C4F74A5A-7083-E511-991A-008CFA0A5808.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6819F16-5683-E511-A052-FA163E1C3E52.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6BB817B-7083-E511-8A20-001B21AEEF2C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC857EAA-8883-E511-94AF-549F35AD8C0A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DCB2292B-6B83-E511-885A-00266CFCCB44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DCCB6053-C083-E511-A2B6-008CFA0A571C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E231E7C8-5383-E511-802A-0CC47A010010.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F21D8002-4E83-E511-B3E0-FA163EDDC215.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F4A664DB-4183-E511-9990-0CC47A00AA80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA6107A5-6E83-E511-B11E-A0369F7FC9C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FCC28148-B084-E511-8F8F-02163E012E9A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1900to1950_mLSP-0to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FCF73E24-B683-E511-9C9D-008CFA0A5684.root' ] );


secFiles.extend( [
               ] )

