import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/04386D4B-0083-E511-9F9B-001E67578C28.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/0873936D-0083-E511-9083-02163E00CA3F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/08BEC90B-FF82-E511-9011-02163E00E5AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/0C38216D-FF82-E511-AF8E-0025903D1B52.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/1A932560-5680-E511-930A-A0369F7FC210.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/20BB387C-0083-E511-A6A1-02163E00BCEE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/20E519EC-FD82-E511-9A54-02163E014D90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/2C241C85-FE82-E511-B8D2-02163E010D1F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/2EF877D5-FE82-E511-8300-02163E013C93.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3A4C4656-FF82-E511-91D3-02163E013B68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3AB9766D-CD82-E511-A5F1-02163E011470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3ED3392D-FF82-E511-822D-001E67579498.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/40EF9063-D682-E511-95B8-02163E015FB5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/42C164A7-5680-E511-BDD5-008CFA0646A4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/48E60580-CD82-E511-AB2C-02163E013CD9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/4A1560A5-EF82-E511-833D-002590494E30.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/4EA725C6-FF82-E511-AAA7-02163E00E623.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/566FE779-CE82-E511-B417-02163E0131FD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5C4A18D2-FF82-E511-9A34-003048F0E2BC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5E8562D6-0083-E511-9297-001E67579498.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5E8898E9-FF82-E511-AB83-02163E014D90.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/661D1CAB-FF82-E511-AE0D-02163E0148C3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/70434BE3-0F81-E511-A24C-008CFA197C38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/76264202-0083-E511-AA6F-02163E01531E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/7A056E0A-D082-E511-BA89-003048F0E84A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/80B295BA-1981-E511-A699-008CFA05E9E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/8E01D724-CE82-E511-9A17-02163E0169DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/9236FADD-CC82-E511-9321-02163E00E843.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/9848587B-CD82-E511-807B-02163E00EA86.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/A6303498-4080-E511-98B6-008CFA1980B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/A8784615-0083-E511-AAB2-02163E016BC6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/B6AADFBE-FF82-E511-A562-002590494E26.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/BC0FF5F1-0083-E511-B54A-02163E01531F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/BC234E63-F280-E511-B981-001E675A69DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/BCE1A638-FF82-E511-9274-02163E014E31.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/C80AB2D7-4580-E511-8950-008CFA580730.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/CC6B87E2-6980-E511-8A85-02163E00EA9F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/DE1EEFC7-FF82-E511-95E2-02163E013112.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/DE88DDCA-FE82-E511-B74D-02163E010F5E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E8F83D86-CD82-E511-9B32-02163E016B45.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/EC3ECC8B-D880-E511-84BE-A4BADB18BC05.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1200_mLSP-1to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F2BD500D-0083-E511-A84B-02163E010E23.root' ] );


secFiles.extend( [
               ] )

