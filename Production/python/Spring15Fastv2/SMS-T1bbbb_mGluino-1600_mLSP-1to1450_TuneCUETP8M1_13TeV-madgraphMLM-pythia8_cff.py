import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/0A372C5C-0E7D-E511-80FF-00266CF23E68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/189F8E5B-0E7D-E511-B025-3417EBE64CB1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C7E135D-0E7D-E511-9BB3-00266CF9C1EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/1C7EF506-0F7D-E511-A81C-485B3919F121.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/221E8C5C-0E7D-E511-8456-00266CF275E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/305EBE63-0E7D-E511-9271-001E67A400F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3224B26B-0E7D-E511-8B97-0026182FD796.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/3A08955B-0E7D-E511-8A2D-3417EBE64CB1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4048D7D7-0E7D-E511-8740-3417EBE645D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/44B4CC5E-0E7D-E511-8AE6-3417EBE520AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/4CC337D7-0E7D-E511-91EB-3417EBE64CB1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/502D8F62-0E7D-E511-9EF9-00266CF97FF4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/569692D6-0E7D-E511-B95A-3417EBE65F56.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5A0B44D9-0E7D-E511-87E3-00266CF25DF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5A667B5B-0E7D-E511-A2B9-3417EBE6471A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/5E77295C-0E7D-E511-996A-3417EBE6471A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/608C31D8-0E7D-E511-9635-3417EBE6471A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/62918663-0E7D-E511-848C-00266CF9C22C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/665D69D8-0E7D-E511-858E-00266CF23E68.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/66FDE75F-0E7D-E511-B44B-001E67A40604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/6CC5BDD9-0E7D-E511-A787-00266CF25DF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7621765C-0E7D-E511-A09E-00266CF25DF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/784A2D5C-0E7D-E511-8277-00266CF25DF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7AD8A25B-0E7D-E511-9844-3417EBE64AFE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7CD57363-0E7D-E511-AC32-001E67A4061D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/7E2EDAD8-0E7D-E511-B655-00266CF275E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/84757866-0E7D-E511-B0FD-001E67A40523.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/84D4515B-0E7D-E511-A9ED-3417EBE6471A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8C88E0D8-0E7D-E511-8476-3417EBE64BAF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/8EE83BDA-0E7D-E511-8901-00266CF9C22C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/981F525B-0E7D-E511-88CF-3417EBE64CD5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A44CF1D7-0E7D-E511-8CA6-3417EBE64CD5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A4617062-0E7D-E511-AE8F-00266CFAE8C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/A86A2D5C-0E7D-E511-A947-00266CF25DF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AC00B567-0E7D-E511-AC2C-001E67A3EB1A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/ACED07D7-0E7D-E511-B77C-3417EBE64AFE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/AE2FAC6C-0E7D-E511-B8C5-001E675A659A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B074A45A-0E7D-E511-B8C2-3417EBE64CD5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B2E86F5A-0E7D-E511-9A50-3417EBE645D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/B8DF71D8-0E7D-E511-B1CE-3417EBE520AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/BC609C60-0E7D-E511-9890-001E67A404B5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C25238E0-0E7D-E511-8227-00266CFAE7E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/C852CC5A-0E7D-E511-8B66-3417EBE64CD5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CE348D5C-0E7D-E511-B960-00266CF275E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/CEAB7C5A-0E7D-E511-9A6F-00266CFAE464.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/D42D395C-0E7D-E511-B543-00266CF25DF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DAE88D5F-0E7D-E511-8BF3-001E67A3EF48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DCE4B65B-0E7D-E511-AE1D-3417EBE64AFE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/DEF86D5C-0E7D-E511-A5C1-00266CF25DF8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/F07C1F83-0E7D-E511-AFE6-0026182FD7A9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1600_mLSP-1to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/30000/FE5A4E63-0E7D-E511-BC26-001E67A4069F.root' ] );


secFiles.extend( [
               ] )

