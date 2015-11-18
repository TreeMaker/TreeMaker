import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/1E754110-3B80-E511-9FBA-0025904A90CA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/469EAF3C-3B80-E511-B371-0025904B2C5C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5618D0E2-3A80-E511-9418-00259048A462.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/5C00F9D5-3A80-E511-9311-00238BCE44F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/66E941E4-3B80-E511-9E2B-02163E014B22.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6AE2F3C6-4080-E511-80AD-02163E014CA7.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6CF678E1-3A80-E511-96FD-002590488694.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/6E4D7DDE-3A80-E511-B58C-0025901D08BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/709C9ED5-3A80-E511-8214-0CC47A13CBEA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/76FC14D6-3A80-E511-B67A-002590EFF972.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/94D485D3-3A80-E511-9457-008CFA1CB73C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/9A0295E0-3A80-E511-BD1B-0025904886E6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/AE80B7DB-3A80-E511-879A-003048344A96.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/CC838EDE-3A80-E511-B3AB-0025901D08BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1275_mLSP-900to975_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/50000/F48537E3-3A80-E511-870D-0025904AC2C0.root' ] );


secFiles.extend( [
               ] )

