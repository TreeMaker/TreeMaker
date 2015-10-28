import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/02A3A7CF-707C-E511-B769-001E67A3EF48.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/06BCE918-467C-E511-9ECA-008CFA198258.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08B03505-687C-E511-B61D-008CFA56D6F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0C391CB8-737C-E511-A0FE-008CFA56D6F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/120ABD84-487C-E511-A5AB-001E675A681F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1C4B82B7-737C-E511-8E16-008CFA01E258.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1C5A67B4-737C-E511-A3FF-A0369F7FC934.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1EBAEF93-637C-E511-9D19-90B11C050AD4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26B71294-457C-E511-AF36-008CFA197B44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2E940A21-6D7C-E511-AE63-008CFA1983E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/32212097-737C-E511-9523-008CFA14F9D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3451A5C4-707C-E511-B364-001E67A3EC2D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/42BF0ADE-6B7C-E511-8C7F-001517FB228C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/483EE88E-537C-E511-8671-001E67A401B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A78BCB8-737C-E511-804C-008CFA1C6564.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A9EB8B9-737C-E511-B6CD-008CFA1CBBA4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C8B049D-737C-E511-BA49-001E67A42A71.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4E006557-697C-E511-99E5-001E67A3EC2D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/52EFB5AE-737C-E511-B5C6-001E675A622F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5801BED2-707C-E511-8321-001E67A3EC05.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5AFF5CCF-707C-E511-AB6A-008CFA197D38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/600DD1CB-737C-E511-BA46-001E67A4061D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/68D52DC8-457C-E511-AD3B-008CFA064774.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6E4A0DB8-737C-E511-ABC4-549F358EB7CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/72099119-677C-E511-A6E0-001E67A42026.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/801F25AA-737C-E511-B18C-E0CB4E2E4E6A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/824397C2-457C-E511-A979-008CFA14FA64.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8248C4FE-687C-E511-8249-008CFA1982C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/862B3470-6E7C-E511-8F99-008CFA1983E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/880B66DD-6A7C-E511-88E7-001E67A3FEAC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9A69CC8D-4D7C-E511-B011-001E675A6AB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9A9FD592-637C-E511-A308-001E675A6630.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9C2B9C11-6D7C-E511-BEFE-008CFA1983E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9C3C1C87-487C-E511-B897-001E67A40604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B6782285-487C-E511-A77F-001E67A40451.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BA972EB7-737C-E511-A24E-008CFA197D38.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC37C517-717C-E511-989C-008CFA1C64B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CE2610FE-707C-E511-ACC8-008CFA197A5C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D815D10B-687C-E511-8451-008CFA1C6458.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DAB6AAE0-6B7C-E511-B5D8-008CFA152104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DEE4F289-487C-E511-9DF2-001E67A401B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E0B47FBC-707C-E511-9255-001E67A3EC2D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2EC6918-467C-E511-9112-008CFA56D794.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4F01CCB-6B7C-E511-8FB1-008CFA0647D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E622A1C7-707C-E511-9823-001E67A3EBD8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EE23DF25-677C-E511-B5C4-001E675A4759.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-875-900-925_mLSP-850-1to875-700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8223F86-4D7C-E511-8057-001E67A3EBD8.root' ] );


secFiles.extend( [
               ] )

