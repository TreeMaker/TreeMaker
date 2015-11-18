import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0445C0C9-3A7E-E511-8DEF-0025905A6088.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/06F3A438-5A7E-E511-BFC9-00248C0BE014.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/0E6B463F-557E-E511-AB28-0025905B857C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1C87A5EA-397E-E511-9749-00248C0BE014.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/249A8572-3E7E-E511-9753-0025905A60A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/328D7A1C-5D7E-E511-A59F-002618943980.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/369BC52E-487E-E511-AF6F-02163E016B72.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/38D88F60-587E-E511-8A48-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/44FA7406-5E7E-E511-8F0E-003048FFCB74.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/507DF434-537E-E511-AC3E-0025905B85AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/521D7D5B-667E-E511-9637-0025905B858C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/525FCC53-647E-E511-9481-0025905A60BE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/58EFF964-677E-E511-B59B-0025905A48C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5A293608-3D7E-E511-9DA8-0025905A60A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5ECAB638-557E-E511-AF0F-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/60418534-537E-E511-896C-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/66C2D6FB-5D7E-E511-9E9C-00248C0BE014.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6836C28E-557E-E511-BBD5-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6CD73221-5D7E-E511-B870-0025905B8596.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6E4E3205-6F7E-E511-9551-0025905B855E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7017D8EC-397E-E511-97AB-0025905A609A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7C62013D-5A7E-E511-9BCD-002590596468.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/7CBDD579-617E-E511-8BDA-0025905A48C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/82FDB921-5D7E-E511-A98A-0025905A60A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8428879D-647E-E511-B17E-0025905A60D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/86FBC90A-3F7E-E511-ADFC-0025905A60AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/886A29A4-3E7E-E511-BBA0-0025905A60A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/886D1301-5E7E-E511-BE51-0025905A613C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/8AEA8152-567E-E511-9388-0025905A6076.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/920C9D82-597E-E511-9D94-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/986C5F56-587E-E511-9A15-0025905A607E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9E81F283-597E-E511-B076-0025905B8596.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A0E37EF1-6E7E-E511-8915-0025905B85A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/A4BCE157-A57E-E511-AB70-0025905A48EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B64DD324-5D7E-E511-B1D2-0025905964A6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/B85E4154-667E-E511-A36A-0025905A60D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C0183F7B-617E-E511-A4A3-0025905B8596.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C2124B22-5D7E-E511-AFD6-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/C69AE035-557E-E511-BC5B-0025905A6084.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D20D6CF0-3F7E-E511-8E02-02163E011603.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/D236D551-567E-E511-B572-0025905B8562.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/DC0E5C04-5E7E-E511-B353-0025905A60D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E0B3924D-677E-E511-98DE-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/E8562898-687E-E511-8E21-0025905B8582.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F251EF8A-687E-E511-87C9-0025905A6094.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-825to875_mLSP-400to825_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F865F921-5D7E-E511-87EE-0025905B8606.root' ] );


secFiles.extend( [
               ] )

