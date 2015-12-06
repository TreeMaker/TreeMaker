import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/02FB971A-7198-E511-AAA2-0CC47A4D99A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/066B132C-7598-E511-85B0-00259073E4DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/069EDBAA-B498-E511-8146-02163E0147F8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0A3BFD6C-7698-E511-9C26-0CC47A4DEE18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0E0BAB4E-6898-E511-BB1C-00259077501E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0E78006D-B998-E511-81C7-02163E013EE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/14D02EF3-6F98-E511-9F11-0025907B4F16.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/18E58C5A-B998-E511-8081-001E67578C28.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1A438CA0-7398-E511-9C01-00259074AEAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/202EFF4D-6C98-E511-9C29-002590D0B074.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/243F747D-5898-E511-9AF0-00259073E4FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/247119A0-5998-E511-A136-00259073E4CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/30B9B19B-B798-E511-86E5-02163E013C74.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/32CCF005-7C98-E511-B062-002590747E40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/346AC806-7C98-E511-A3AB-002590D0AF7C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3CB90D9C-5998-E511-B706-002590D0AFFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4AC4394E-7B98-E511-8401-20CF305B055B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/501C66C1-B498-E511-9DC4-02163E010F60.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/50C18A65-7498-E511-B68F-00259074AE32.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5247D51D-7198-E511-B061-00259073E3AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/586DC0F1-B298-E511-9CC9-02163E014CF1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5A217A7B-B998-E511-9BC2-02163E0147AC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5A346375-B998-E511-9EE1-02163E00EAB4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5C5AF5D3-7D98-E511-848C-002590747E40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5E9743E9-B298-E511-BBB4-02163E014D34.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/744FA44C-6C98-E511-A6D7-002590D0AFEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/88E230A3-7398-E511-8E61-00259074AE32.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/900D0829-7598-E511-8FF2-0CC47A4DEE18.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/9059A6DA-B598-E511-AD31-02163E010C95.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/90B9837D-5898-E511-97E1-00259073E4E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/92066D80-5E98-E511-B7A9-00259074AE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/963C614E-7B98-E511-88AC-00259073E37C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A62292ED-B498-E511-97AE-02163E010F0B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A82ECDB5-B798-E511-8C0C-02163E013E7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/ACF2A209-B298-E511-B0CB-02163E011767.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AED890B4-6D98-E511-B5B6-002590D0B074.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BC575240-7098-E511-A9B8-0CC47A4D99B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/BE8D208E-7698-E511-B6B1-20CF3027A57B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C4AD9800-B698-E511-A9D3-02163E00E7F1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/CA92FB28-6D98-E511-BB76-00259073E3A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/CE06331D-B598-E511-BA2A-02163E013BE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E6EFD54D-6898-E511-B9A5-00259073BBF6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F23C6529-6D98-E511-B953-00259074AEAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F2E3FA67-7498-E511-A80A-20CF3027A57B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1200to1225_mLSP-1to1175_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/F6B9EE24-B298-E511-9695-02163E0117D1.root' ] );


secFiles.extend( [
               ] )

