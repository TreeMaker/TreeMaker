import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/0CC1F17D-DD8A-E511-99B0-0CC47A78A4B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/1EE01E7A-DD8A-E511-85F1-0025905B858C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/382FB17E-DD8A-E511-A048-0CC47A78A4B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/3EE8669F-FF8C-E511-B0A8-6CC2173BBAA0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/50CDED99-FF8C-E511-A8F4-C4346BC8F6D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/5847599D-FF8C-E511-A5DC-C4346BBCB408.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/8279FA7D-DD8A-E511-B5B3-0CC47A78A3F4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/A0E07A78-DD8A-E511-8352-0CC47A4D769E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/B8162B7A-DD8A-E511-9663-0025905A6104.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/BAD4CD76-DD8A-E511-A2D7-00261894396D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/D2C07976-DD8A-E511-9A9B-0026189437EC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/F6E8EA99-FF8C-E511-B3F1-C4346BC8F6D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1qqqq_mGluino-1175_mLSP-975to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/10000/FC884879-DD8A-E511-895E-0CC47A78A41C.root' ] );


secFiles.extend( [
               ] )

