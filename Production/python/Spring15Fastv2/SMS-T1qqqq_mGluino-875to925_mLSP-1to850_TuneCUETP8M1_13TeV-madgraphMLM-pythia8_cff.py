import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/029C81C3-2894-E511-8B05-0CC47A4C8E3C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/02E431CB-2894-E511-B975-00261894396B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1C754890-2994-E511-87C6-00261894397F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1C9FADC5-2894-E511-AF8B-0CC47A78A32E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1E22878E-2994-E511-B423-0CC47A78A456.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/1ED107C4-2894-E511-8DC7-0CC47A74525A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/20B2A2C8-2894-E511-8965-0025905A48C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/241A4992-2994-E511-A7AE-0CC47A4D769C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2497EEC5-2894-E511-B155-0CC47A4D7604.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/287E088E-2994-E511-A840-0CC47A78A436.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2C68C8C7-2894-E511-A1EC-0025905A60D2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/325A46C5-2894-E511-95E8-0CC47A4C8E86.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3CE8B9C8-2894-E511-A5E7-0025905A6118.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4AFF9990-2994-E511-8BF1-0CC47A4D764C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4C6B56C6-2894-E511-924B-0CC47A4D76A2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/56229E8F-2994-E511-8385-0CC47A745284.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5A9526C3-2894-E511-9B1C-0CC47A78A360.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5C05D38F-2994-E511-80CE-0CC47A745250.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/5CA27CC7-2894-E511-8F30-0025905A6092.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/60C8578F-2994-E511-AB0C-0CC47A78A42E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/64EB2B8F-2994-E511-8E73-0CC47A78A456.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6616ABCA-2894-E511-88D9-003048D15E0E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6CF6A98F-2994-E511-B54C-0CC47A4C8E86.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/70202893-2994-E511-8772-0025905A611E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/74E514C5-2894-E511-AC04-0CC47A78A2F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/884C90C9-2894-E511-8CA5-00261894390B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/9655508D-2994-E511-AFB4-0CC47A4D768C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/9CE788C2-2894-E511-8940-0CC47A78A42E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A82B9D8F-2994-E511-83F9-0CC47A4D7634.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A8C0F2C3-2894-E511-8FD5-0CC47A4D7694.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A8F0DFC4-2894-E511-BC3B-0CC47A4D7674.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AE5C7292-2994-E511-89E1-0CC47A4C8E16.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AE8739C4-2894-E511-BF94-00261894384F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AEBBC490-2994-E511-B2C5-0CC47A745298.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/B6889B8F-2994-E511-8837-0CC47A4D760C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C282BCCD-2894-E511-A2D4-0CC47A78A4A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C2EBF28C-2994-E511-9B94-0CC47A4D768C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D0799292-2994-E511-A737-002590593878.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D41C37CA-2894-E511-B825-003048FF86CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/D6894E8E-2994-E511-AD41-0CC47A78A45A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/DAD8458F-2994-E511-9206-0CC47A4C8E56.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/DE4B8BC9-2894-E511-8C3F-00261894390B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/DE99C88D-2994-E511-A0FD-002618943948.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E0B6308E-2994-E511-86B4-0026189437E8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E44EE1C4-2894-E511-8406-0CC47A74525A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E83CBF8F-2994-E511-96DD-0CC47A4D76AA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E8967BC5-2894-E511-ADD0-0CC47A4D765E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/FEC83DC5-2894-E511-9034-0CC47A4D75F6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-875to925_mLSP-1to850_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/FED7F291-2994-E511-9E01-0CC47A4D7670.root' ] );


secFiles.extend( [
               ] )

