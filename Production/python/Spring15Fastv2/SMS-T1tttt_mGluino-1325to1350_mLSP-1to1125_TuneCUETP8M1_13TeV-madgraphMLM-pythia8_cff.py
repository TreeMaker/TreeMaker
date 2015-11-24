import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/004E3501-C88A-E511-B4A1-02163E00B2BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/00E5729B-B38A-E511-951B-02163E00EA46.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/02A6976A-E38A-E511-9208-02163E016BEC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0EB535F0-9F8A-E511-B45B-02163E01686F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/18A5723C-9F8A-E511-A659-002590DE6E3C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1AA72409-0D8B-E511-88EE-02163E00EA6E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1C72AAD3-B88A-E511-9E4C-02163E00CEB5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/20B8B2BC-C88A-E511-884A-02163E012D49.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2A2EDD2E-CA8A-E511-8B57-02163E016B43.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2C400D3E-0D8B-E511-8331-02163E014DFF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/40B9CCFD-C98A-E511-A6A4-02163E014855.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/50F2051F-A98A-E511-AE2C-02163E00CA3F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/52F89DF6-BD8A-E511-A507-02163E00B090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5636F897-AD8A-E511-8314-02163E00E6D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5C8DBD24-A98A-E511-A2E6-02163E016B62.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/60B35B6F-A08A-E511-90FE-008CFA111358.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/683063F5-058B-E511-9EAB-02163E01342F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6CF74735-998A-E511-890E-02163E011638.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/72191930-EB8A-E511-A39A-0CC47A00AA80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7626B686-958B-E511-84CF-02163E00EA9A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/768CE440-E38A-E511-AA1D-02163E00F4CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/76FFB215-3B8B-E511-9DA6-02163E014D90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/78485F47-B38A-E511-B7A1-02163E00CE87.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7A66C38B-A48A-E511-BA89-008CFA111270.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7A83571B-A08A-E511-BB4D-02163E011515.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/845B3279-AD8A-E511-8B21-02163E01147F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/88556D7F-A08A-E511-80FF-02163E011442.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9A084575-A98A-E511-9666-02163E013E8D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9E81FBF5-3A8B-E511-BBF9-0CC47A04CFFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A815306E-B98A-E511-A4C3-02163E00F521.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AE3CF5D1-B88A-E511-A69C-02163E00E816.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B2D34C19-068B-E511-925A-02163E013D74.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C4D95A27-BE8A-E511-BCDB-02163E016BFD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D493E586-C88A-E511-976F-02163E012CE7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DE7A65B1-C88A-E511-B065-02163E012D49.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E05F0FEF-9F8A-E511-A2A9-02163E0139FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E6456670-9F8A-E511-B356-02163E00EA38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EC6C2652-AD8A-E511-85F5-02163E00CA3F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FC8F59CB-B98A-E511-99E5-02163E016B25.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/4E500B81-DC8E-E511-A703-02163E012EFC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5EAB4586-DC8E-E511-919B-0025901AF54E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/90784F73-DC8E-E511-93B4-02163E010EF7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/C27699A3-DC8E-E511-A2B5-02163E013D51.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/D23B8790-DC8E-E511-B582-02163E012A12.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/E4DC09A1-DC8E-E511-8FEA-02163E016BD3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1325to1350_mLSP-1to1125_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/F8301A83-DC8E-E511-9B94-02163E011B26.root' ] );


secFiles.extend( [
               ] )

