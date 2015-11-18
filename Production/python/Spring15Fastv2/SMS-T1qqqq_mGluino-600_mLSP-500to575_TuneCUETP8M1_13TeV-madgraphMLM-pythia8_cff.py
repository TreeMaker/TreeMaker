import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/00AA5159-637E-E511-809B-002590D9D8D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1C82AD68-637E-E511-AE5B-002590D9D8C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1CED2D5F-637E-E511-AE4D-002590D9D976.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2042B3A7-647E-E511-8145-002590D9D976.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/224FBA6A-637E-E511-B3A2-002590D9D9F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/26F3A54F-637E-E511-BD6F-002590D8C7E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2CD3654F-637E-E511-97CF-002590D6005C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/34CF094D-637E-E511-B24B-001EC9ADE177.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/364EA067-637E-E511-B3BB-00304867FD3F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3691319D-637E-E511-A48F-0CC47A0AD704.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/402EB134-647E-E511-AC25-002590D9D8BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4C159743-637E-E511-AD85-001EC9ADDBB9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/50EA114F-637E-E511-81AD-002590C14CD2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5657B745-637E-E511-804A-001F2965D25E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/567CE58D-637E-E511-9AC3-0CC47A0AD6E4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/584A1647-637E-E511-A10D-002590E50AF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5E70644F-637E-E511-801C-002219560610.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6CDD9543-637E-E511-BFDA-20CF3027A62B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6E45D46D-637E-E511-827F-002590D9D92A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/72B26C5A-637E-E511-98DE-0026181D291E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7866E347-637E-E511-86DC-001F296524E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7873C26A-637E-E511-A93A-0025901AC0FA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7C55FC54-637E-E511-9B2F-001EC9ADC50F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/82E1AF8B-647E-E511-9258-0CC47A0AD630.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/862B0855-637E-E511-AF74-001EC9ADEA9B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/883E0A7A-637E-E511-A5EE-0CC47A0AD780.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8EB7714D-637E-E511-B7B4-002590D4FBB6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/965EB546-637E-E511-A0EA-A4BADB3CF272.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96BCD54F-637E-E511-9FE8-001EC9ADD74F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96E70144-637E-E511-BBC5-B083FED13803.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9A210F44-637E-E511-964A-B083FED138B3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A04DEE5F-637E-E511-8BBB-002590D9D84A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6195342-637E-E511-AC72-20CF3027A561.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A64F3E93-647E-E511-AE96-0CC47A0AD630.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C8C72860-637E-E511-96C9-001EC9ADE299.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D0743FB6-647E-E511-A64C-00304867FF1B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D4BBAF5B-637E-E511-B93C-001EC9ADDB5F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DA6176B5-647E-E511-85B1-0CC47A0AD668.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DC3DA06D-637E-E511-A703-00259029ED0E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/EAD8654F-637E-E511-A496-0025900EB500.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F0F8324D-637E-E511-B689-001EC9ADCBEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8EAF945-637E-E511-9086-001EC9ADDD58.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA907F4F-637E-E511-BA88-001EC9ADDBFF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FAB7A147-637E-E511-8581-00259073E520.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-600_mLSP-500to575_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FE345A63-637E-E511-AD08-00304867FF1B.root' ] );


secFiles.extend( [
               ] )

