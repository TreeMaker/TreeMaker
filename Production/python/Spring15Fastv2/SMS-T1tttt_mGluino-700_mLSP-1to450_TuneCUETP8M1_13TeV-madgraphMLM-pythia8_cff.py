import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/004B74C6-8A80-E511-8670-00259073E31C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/009D677F-9180-E511-8C4D-02163E015FAA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/046D0E6F-8B80-E511-BD73-0CC47A4DEE04.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/10A44FD5-8780-E511-BCEA-00505602078C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/1CF26E96-9380-E511-969A-02163E013B17.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/22E991F5-8780-E511-847E-20CF3027A600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/26B252E4-8D80-E511-BE1F-002590747D92.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/2C0575C6-8A80-E511-BE10-00259073E31C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/2CD638EC-8980-E511-A4F7-20CF3027A600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/32683B5D-8D80-E511-8F83-0CC47A4DEE04.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/345363A2-8880-E511-8D80-00259073E3AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/348CCC88-8C80-E511-AF00-549F358EB77C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/34DE637D-8680-E511-B478-485B39897219.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3655D9D9-8B80-E511-9D05-005056020786.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3AD37A8C-8D80-E511-9C67-485B39897219.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3CAFF2C5-8580-E511-B9D4-0CC47A4DEEFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3E7E25E8-8C80-E511-A2B6-00259073E31C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/40599659-9180-E511-9F8A-02163E00BFA3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/4264B07E-8B80-E511-9588-BCAEC53F6D4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/4C2858C6-8C80-E511-BC96-00259073E31C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/4EFD43AD-8880-E511-9150-00505602078C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/52604582-8C80-E511-8CFC-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/56F00A7E-8C80-E511-8D3C-549F35AE4FA2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5AE8B07D-8B80-E511-9385-A01D48EE8350.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/602282D2-8980-E511-B2CC-BCAEC53F6D4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/64E8CE86-8C80-E511-99AD-0CC47A4DEE36.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/6C1A1229-8B80-E511-8074-00505602078E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/78BF2E96-8C80-E511-87AA-003048895D40.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/7EF3B81E-8B80-E511-9418-BCAEC5097212.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/82632117-CB7F-E511-89EA-485B39897219.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/828D1B8B-8780-E511-B84E-0CC47A4DEEFA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/82CBF525-8E80-E511-8959-00259073E31C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/86C8D59B-8C80-E511-BE98-005056020785.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/86F1D9CA-8A80-E511-B0B0-008CFA0A58B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/8A5D33F0-8780-E511-B347-BCAEC53F6D4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/94CB5696-8780-E511-A1FE-485B39897219.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/A81E49AB-8C80-E511-9F97-BCAEC5097212.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/AE4900C5-8580-E511-B026-BCAEC53F6D4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/B6B9E405-8E80-E511-9D4C-BCAEC5097212.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/BE69CA86-8D80-E511-AFF6-BCAEC53F6D4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/C2D9C0B8-9180-E511-AE09-02163E0168E2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/CC37E817-8A80-E511-A855-0CC47A4D99B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/D019A0DF-8D80-E511-8584-20CF3027A600.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E0B9DD89-8C80-E511-9520-001E672483D1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/E67259E7-8A80-E511-9ABB-008CFA1980B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/EE43A08D-8D80-E511-9FA4-00259073E456.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F0FBF17E-8680-E511-B247-00259073E3AE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-700_mLSP-1to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F6D59BC3-8A80-E511-A34D-0CC47A4DEE36.root' ] );


secFiles.extend( [
               ] )

