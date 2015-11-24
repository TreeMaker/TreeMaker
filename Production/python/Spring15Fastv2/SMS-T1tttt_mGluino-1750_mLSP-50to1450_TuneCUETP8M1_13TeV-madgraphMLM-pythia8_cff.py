import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/02F86BB8-098C-E511-9952-02163E013CB4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/069F7EEB-138C-E511-9604-00259073E3B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/06D66EE8-0D8C-E511-B3E0-A01D48EE8012.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/18CDA8F3-008C-E511-A738-002590D0B052.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/1E1EB2F2-008C-E511-838A-0CC47A4DECD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/2677FCF2-138C-E511-B21D-005056020787.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/3A33B4DF-0D8C-E511-A39E-00259073E4E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/44C2EA18-388B-E511-826E-0025907B4F44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/4699D2F2-008C-E511-A3B7-002590D0AFCA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/56111FDF-0D8C-E511-B098-002590747DF0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5842D2DF-0D8C-E511-8029-002590D0B0CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5A2F5A5D-AA91-E511-AE3E-D8D385AE8862.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/5E347B9E-F48B-E511-A402-002590747DE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/6299619F-F48B-E511-A519-00259073E450.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/6A81E350-E58B-E511-AD73-005056020780.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/6E82AC86-098C-E511-81C0-02163E00EA99.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/6EA354EA-138C-E511-9752-002590D0B09E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/72F215F3-008C-E511-8EB6-0025907B4F9A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/7C8D8645-168C-E511-9F47-02163E01664D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/7CAF204D-208C-E511-B91B-20CF305B0572.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/8006044B-208C-E511-946C-002590747D94.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/80554DEC-138C-E511-AC76-00259073E4AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/8A65619F-058C-E511-A2D5-00259073E36E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/8E62049E-F48B-E511-8F5F-0025907B4F4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/9044ADEC-138C-E511-BFFF-20CF3027A5E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/92D358DE-0D8C-E511-BD34-002590D0AF6C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/98B9C3EA-138C-E511-AE54-0CC47A4D9A3A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/B031F9F1-008C-E511-95D5-0CC47A4DEDA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/B4147BD9-198C-E511-90EF-02163E016A45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/B43F51E4-1C8C-E511-80E1-02163E016BAB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/D21380EA-138C-E511-8651-0025907B50FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/E0447148-178C-E511-A086-00259073E450.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/EA0ADFDA-0A8C-E511-B471-00259073E35A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/EA1F37A0-058C-E511-AA13-0025907B4F4A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/F402A3ED-138C-E511-97AD-20CF305616D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1750_mLSP-50to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/70000/F8FB9748-178C-E511-AEFC-002590747DD8.root' ] );


secFiles.extend( [
               ] )

