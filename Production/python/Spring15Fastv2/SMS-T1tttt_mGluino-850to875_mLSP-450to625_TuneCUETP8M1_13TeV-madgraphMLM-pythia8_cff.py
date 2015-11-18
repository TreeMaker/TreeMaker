import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0051F802-4E83-E511-AC46-FA163EF858EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/12C7A8D4-7083-E511-B1C7-0002C92A1034.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/24AEA46C-4D83-E511-94E2-02163E016BCC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2E38A021-8183-E511-8AE0-24BE05C6E561.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3061C197-AF83-E511-B139-20CF305616E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/324246DC-4E83-E511-A913-5065F381E251.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/368078C6-5884-E511-BBE5-02163E016BC8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/36ABC6CA-5884-E511-9B0C-FA163E928EE8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A578CF5-A983-E511-AC30-00259021A526.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3AF06C11-5183-E511-8787-02163E010F32.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/449522B4-8583-E511-B987-B8CA3A708F98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/48E648CA-8583-E511-805B-68B599B49E25.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4A180D3F-5984-E511-A5F7-0025904B1FBE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/507BF603-7A83-E511-96F7-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/52AB4DAA-5884-E511-BFE3-001E67504FED.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/52B3F7D5-4E83-E511-BA46-5065F3817221.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5844B217-8983-E511-8EE1-5065F3816291.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/58496231-B083-E511-9E16-00505602078B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5E7DFAFC-8583-E511-9D6A-24BE05C488E1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/60D97B18-B383-E511-8EFD-FA163E2D0A91.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/622F5CDF-5884-E511-8B47-02163E013C7E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6429BBB0-C383-E511-98A8-00259073E334.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6C598855-5B83-E511-8D1A-FA163EFF5FD3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6CED22FE-7983-E511-99ED-A0000420FE80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/76D78CFC-7C83-E511-9036-68B599B58825.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8059FAA9-5383-E511-8268-02163E0115EF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8820C2CC-B783-E511-8A5C-901B0E542756.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/94728653-8783-E511-89E0-24BE05C44BC1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/96926241-8783-E511-B1C9-5065F3816291.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/982172FB-7C83-E511-9E1C-24BE05C4D8F1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A0DFB95C-6383-E511-895F-FA163EFF5FD3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6083DAD-6F83-E511-8826-02163E00C022.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A67AD07C-8B83-E511-90E8-24BE05C45BF1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B0F7FAE5-5283-E511-81BF-02163E013F1E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BC52E986-4D83-E511-9995-02163E014ADB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BE9393D5-7083-E511-89E6-0002C92DB4CE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BEEE447A-6F83-E511-9C45-FA163EC607D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2D13052-5B83-E511-B32D-02163E010FA1.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C609CCBF-5B84-E511-9160-02163E011529.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C6BE98D5-B083-E511-AA99-001E67581344.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D83F4D12-5984-E511-AE1B-02163E013A91.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4347C02-4E83-E511-B788-FA163E906448.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E6B92CBF-A983-E511-AFA7-00259022516E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F4A23290-8B83-E511-92F2-24BE05C33C71.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-850to875_mLSP-450to625_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F86E5A47-AF83-E511-8E07-20CF3027A5C5.root' ] );


secFiles.extend( [
               ] )

