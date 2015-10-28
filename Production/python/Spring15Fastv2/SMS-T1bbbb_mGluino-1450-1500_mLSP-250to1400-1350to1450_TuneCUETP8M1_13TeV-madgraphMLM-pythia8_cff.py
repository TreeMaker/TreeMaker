import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0ABBDC70-7B7B-E511-8183-F45214C748C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/1A69C928-7D7B-E511-9F17-0002C92958E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/20182FAB-7B7B-E511-8ED3-24BE05C6E591.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3014C086-7B7B-E511-9502-0002C94CDAE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3049B6F6-807B-E511-ADCD-24BE05C6E571.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/32507452-817B-E511-BCEE-F45214C748C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3C7F9289-657C-E511-B940-441EA158FE9A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48B2F62E-7D7B-E511-998D-F45214C748C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48B7C975-7C7B-E511-85F7-F45214C748C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5689AA6E-7C7B-E511-A306-24BE05C48801.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6AB811E4-7A7B-E511-9715-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6C752272-7C7B-E511-A23A-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6C8C8B4C-817B-E511-A7F9-0002C92DB45C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6C9FB57E-7B7B-E511-84E8-0002C92958E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6ED46771-7C7B-E511-8E1E-F45214C748D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/72E4B24E-7C7B-E511-ABE7-0002C92DB470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7483F119-817B-E511-AC13-0002C90F8030.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7621872E-7D7B-E511-BC11-0002C92958E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7A317F73-7C7B-E511-8BBA-0002C92DB530.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E668075-7C7B-E511-9D47-0002C92DB470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8236A8B6-7B7B-E511-AB05-0002C92DB530.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/88053832-7D7B-E511-8555-0002C92DB4CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/88D5F63F-7C7B-E511-92B5-24BE05BD4F61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9096F06D-7C7B-E511-830E-5065F381E251.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9443D937-7D7B-E511-81E6-24BE05C48801.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9834940A-7D7B-E511-AB07-24BE05BD4F61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9C145575-7C7B-E511-90BF-F45214C748CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9CF84D75-7C7B-E511-B242-0002C92DB45C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9E06E192-657C-E511-8007-0030487C116E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A2B3E2E4-7A7B-E511-9679-F45214C748D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B0BF4830-7D7B-E511-92D8-0002C92A1034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C0C954F3-7A7B-E511-8787-F45214C7493C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C0E56F19-7D7B-E511-A158-5065F3812221.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6E9D171-7C7B-E511-832E-5065F3812221.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA58E545-817B-E511-90A6-0002C92A1024.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA601775-7C7B-E511-9FED-F45214C748D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CC592662-7B7B-E511-B162-24BE05C6E7C1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D4B4B130-7D7B-E511-8B52-F45214C748C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D8D192B2-7B7B-E511-9AA8-0002C90F8094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DEEFE02F-7D7B-E511-8CAE-F45214C748B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E0263B3E-817B-E511-8600-0002C92DB530.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E0BFCCEC-7A7B-E511-8C1A-24BE05C6E591.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E42B8E6A-7B7B-E511-93D3-F45214C748CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E600E0AF-7B7B-E511-8C7D-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6395875-7C7B-E511-A97D-F45214C748C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6BDC9E5-7A7B-E511-8926-0002C92DB470.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F6EE5CE5-7A7B-E511-AA12-0002C92A1034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F8DA9974-7F7B-E511-BDD1-24BE05C6E561.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA5E0478-7C7B-E511-BF88-24BE05BDBE61.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FA7DCDF9-7B7B-E511-BD05-F45214C748C8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-1450-1500_mLSP-250to1400-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FC33E5F7-807B-E511-B934-0002C92DB4CC.root' ] );


secFiles.extend( [
               ] )

