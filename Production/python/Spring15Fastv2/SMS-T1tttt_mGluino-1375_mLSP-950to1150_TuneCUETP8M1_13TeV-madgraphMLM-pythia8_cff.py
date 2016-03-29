import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/04C3D33A-CD93-E511-B8C8-0025907DCA72.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/04DCE537-CD93-E511-838C-002590DB9302.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/08BFB337-CD93-E511-9D97-E41D2D08E0A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/0C135D3B-CD93-E511-9794-002590AC5060.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/245DA248-CD93-E511-9401-0025904E32F2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/24A37836-CD93-E511-A10D-002590AC4C76.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/2E843039-CD93-E511-894E-047D7BD6DF32.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/36FF7737-CD93-E511-9DAA-002590DB053C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3A84F837-CD93-E511-AE1B-F45214938700.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/3E729846-CD93-E511-86CA-0025904B1370.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/40C9513E-CD93-E511-AB75-0025907DC9C6.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/44C9BD37-CD93-E511-9490-002590DB91C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/4CE45333-CD93-E511-8DDF-E41D2D08E0A0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6CA99435-CD93-E511-8787-E41D2D08E090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6E704746-CD93-E511-BE86-00A0D1EE05D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/6E9CA336-CD93-E511-B9ED-E41D2D08E0B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/8005C53A-CD93-E511-9318-0025904B12B2.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/8087A136-CD93-E511-956F-E41D2D08E0B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/8AC0CBC8-CD93-E511-A431-E41D2D08E0B0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/9834C147-CD93-E511-9212-0025904B1370.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/98408E37-CD93-E511-9074-FACADE000140.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/A8363035-CD93-E511-B16F-E41D2D08E090.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/AE29763C-CD93-E511-A5D0-001DD8B71DB8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/C0E43B36-CD93-E511-82AB-002590DB9302.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/E2228636-CD93-E511-B94A-E41D2D08E050.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-1375_mLSP-950to1150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/00000/FA489336-CD93-E511-B8F1-F45214938700.root' ] );


secFiles.extend( [
               ] )

