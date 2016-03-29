import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/046763D6-1982-E511-8798-38EAA7A6D65C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/08B86AB9-4981-E511-9272-02163E00E63B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/30046584-1982-E511-91AA-001E6739B859.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3085479E-4C81-E511-80B6-FA163E0FB63F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/3A71C2A5-4C81-E511-98B3-FA163E50C94E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/501E96B4-4C81-E511-A845-FA163EA28BB3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5038891C-4B81-E511-A929-FA163E0FB63F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/52187FB6-4C81-E511-AC0D-FA163EA65750.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5AC21AB4-4C81-E511-8F11-FA163EA28BB3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/5AEAA298-4981-E511-8076-02163E00E5CF.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6A4055B4-4C81-E511-9124-FA163EA28BB3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6CC41AB4-4C81-E511-98B7-FA163EA28BB3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/78F821BA-4A81-E511-96E2-001E67578FA8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/8290B3CC-4A81-E511-8FAA-02163E0135B6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/98F2EE9E-4C81-E511-ACDE-FA163EFE6027.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/A6828A8F-4A81-E511-BA52-02163E0139FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/AAFB3CA0-4B81-E511-B54B-02163E00E5BB.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ACF7BA64-1E82-E511-81D0-003048322A2A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B08A9692-1E82-E511-A7A0-00304867FCE3.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B4FDE207-4B81-E511-AFCA-FA163E0FB63F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/BEDC6F88-4A81-E511-B29C-02163E013D7B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/DEC03A9E-4C81-E511-A632-FA163E0FB63F.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E0ED4AA0-4C81-E511-A194-FA163E5369B5.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-975_mLSP-600to750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/E65EE5F4-4A81-E511-A2B8-0CC47A04487C.root' ] );


secFiles.extend( [
               ] )

