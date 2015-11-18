import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/020F53B3-FA7E-E511-A3E7-0025901D4B06.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/042DD2AF-FA7E-E511-A6A9-002590DB9216.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0CC7F6B1-FA7E-E511-98D9-0026189438DF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/2EF362B1-FA7E-E511-A5C6-0025905B85E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/303D3BAB-FA7E-E511-9E28-002618943874.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/307A8EB1-FA7E-E511-A9A9-002590AC4FE2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/340392B2-FA7E-E511-B78B-047D7BD6DE14.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3408B0B2-FA7E-E511-9AA9-002590DB053C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3AEAF1B0-FA7E-E511-8020-0025905A60D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/40CEFBB7-FA7E-E511-98B1-002590D94F8E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/502C75B7-FA7E-E511-AC8C-047D7BD6DD4C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5E7B68AD-FA7E-E511-9F4C-002618943807.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/609638AC-FA7E-E511-9FD4-002618943930.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6EB75AB0-FA7E-E511-8BE2-0025905822B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6EBCD0CB-FA7E-E511-836F-047D7BD6DE1E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7E392964-FA7E-E511-9010-00261894382A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/843FCBB0-FA7E-E511-8D16-0025905B8568.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/849B0CB4-FA7E-E511-89F2-0025907DC9D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/869EB8B2-FA7E-E511-A44E-0025905B861C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8AB152BB-FA7E-E511-B5BC-0025905A60B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8ABFC3AF-FA7E-E511-898D-00261894389A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8C9465AF-FA7E-E511-BC5A-0025907FD2DC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8E15C2AC-FA7E-E511-9470-0026189438AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/9A1A9AAF-FA7E-E511-BD61-E41D2D08DD10.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A018E6AF-FA7E-E511-A473-002618943950.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A2F3C4B2-FA7E-E511-A9A0-002590DB9298.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AA7AB6AF-FA7E-E511-AE12-047D7B881DAE.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B22162B4-FA7E-E511-B2EC-0025905B85F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B266C1AB-FA7E-E511-BC8B-0026189438D6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B4CD91AE-FA7E-E511-A663-E41D2D08DD80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B61EE1A2-FA7E-E511-B9E3-0025907FD3CC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B8DEF6B6-FA7E-E511-9C5A-003048FFD7D4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C2576CB4-FA7E-E511-A7F9-002590593920.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA3795B2-FA7E-E511-B9D2-0025905B861C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CAA359AF-FA7E-E511-8101-002618943919.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CE99E4B1-FA7E-E511-AD0C-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D2C40FB2-FA7E-E511-BF15-002590DB9286.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D2D367AF-FA7E-E511-958D-00266CFFA5C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DE504FB2-FA7E-E511-B946-047D7BD6DE44.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E22FFAB0-FA7E-E511-9229-0025905A612E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E2BCF9C9-FA7E-E511-9A24-0025905A60CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E47C4CB5-FA7E-E511-9168-0025905B85F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E4E8C1BA-FA7E-E511-8EDF-047D7B881D98.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E61D04B0-FA7E-E511-8FA5-0026189438B9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F430F8B3-FA7E-E511-BEF5-002590DB9196.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/F43197AF-FA7E-E511-9DC2-047D7BD6DDF2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FAA859B1-FA7E-E511-9E14-0025901D4844.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1450to1475_mLSP-50to1075_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/FCB995B2-FA7E-E511-8E6E-0025905B861C.root' ] );


secFiles.extend( [
               ] )

