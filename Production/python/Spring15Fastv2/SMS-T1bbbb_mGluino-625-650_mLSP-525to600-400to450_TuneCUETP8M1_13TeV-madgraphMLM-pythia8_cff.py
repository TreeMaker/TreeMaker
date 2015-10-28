import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/024A63ED-7D7B-E511-836B-003048FFD79C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/06869E48-7A7B-E511-A6F1-0025905A6136.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/0EBA93FC-807B-E511-B5C4-0025905A608E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1259C2EC-7D7B-E511-A00A-0025905964B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/14E0BC9F-AB7B-E511-BF94-002590207E3C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/1C80D646-7A7B-E511-8352-0026189438E9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/20DA3DF8-807B-E511-A2BA-00261894389D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/247A34ED-7D7B-E511-877A-0025905A608A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/26A4684A-7A7B-E511-98AB-0025905A60D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2AAD78F2-7D7B-E511-8C8D-0025905A6138.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2ADBEB4A-7A7B-E511-A325-0025905A497A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/30C0A5F7-AF7B-E511-B9BD-20CF3019DEF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/36B9F3EB-7D7B-E511-B777-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/36C976FB-807B-E511-9BD3-0025905A48BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/4E38D84B-7A7B-E511-BB42-002618FDA279.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/508474B7-AB7B-E511-AFB6-001E6757EAA4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/52FAC349-7A7B-E511-9B92-002590596498.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5AC86811-B07B-E511-B507-001E67504A65.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/6A3E1448-7A7B-E511-BED0-002618943886.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/70813D4E-7A7B-E511-A73C-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/70B4A314-7A7B-E511-A9B2-0025905A609A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7C35D781-AB7B-E511-B716-001E675047A5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/7CE34FED-7D7B-E511-AAC7-0025905B8590.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/8448E611-B07B-E511-AEE6-001E67505105.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/88B14549-7A7B-E511-98C1-003048FF9AA6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/92A54145-7A7B-E511-B948-0026189438D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/98D7E44B-7A7B-E511-BAFB-0025905A60B4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A0BC9E4A-7A7B-E511-8862-0025905A60DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A6533206-7A7B-E511-A3EE-0025905B858C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A86E5EFC-807B-E511-8C07-003048FFD756.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/AC4387EE-7D7B-E511-A5D0-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/ACF63351-7A7B-E511-BD3E-0025905822B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B068514A-7A7B-E511-BEAE-003048FFD756.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B0D5B749-7A7B-E511-96B8-0025905A609E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B2477311-B07B-E511-8696-001E67504A65.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B8632FED-7D7B-E511-828A-0025905964BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/B874294A-7A7B-E511-A3B2-0026189438DD.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/BC0C1D0C-B07B-E511-8B60-001E6757E05C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/CCAF1645-7A7B-E511-BA67-00261894397F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/CE3E6245-7A7B-E511-BBA1-005056020788.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/CE5A3D4E-7A7B-E511-BCF7-002590596484.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/CE9BCF48-7A7B-E511-BB7F-0025905A6136.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/D2ADA8EC-7D7B-E511-8EAC-002590596486.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/DE69724A-7A7B-E511-8968-0025905A60DA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E0081357-817B-E511-BF8C-0026189438E9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/E6F9AEEA-7D7B-E511-A445-0025905B85EE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EC05C845-7A7B-E511-A33A-0026189438D7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EE1CB5EB-7D7B-E511-A5F4-0025905964B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F020EBC2-AB7B-E511-A7C1-001E675811CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/F42ECA49-7A7B-E511-84BA-0025905A608C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-625-650_mLSP-525to600-400to450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/FC2A8C47-7A7B-E511-938C-0025905A6080.root' ] );


secFiles.extend( [
               ] )

