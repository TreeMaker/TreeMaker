import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/089F9192-A17E-E511-836A-002481ACEA80.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/08FB806A-A17E-E511-94CA-002590D9D976.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/40B1597F-A27E-E511-A993-0CC47A0AD6FC.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/42A25F73-A17E-E511-8381-002590D9D98E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/5AC03BA7-A17E-E511-9699-001A648F1A4E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/7E3BFD00-A17E-E511-BBA5-001E67E6F783.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/84559D63-A17E-E511-A04C-002590A371C4.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/AA60874D-A17E-E511-A40A-002590FD5122.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C23D26BE-A17E-E511-AE32-002590D9D8B8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/C80DD66F-A17E-E511-AE11-002590D9D8BA.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/D6B48362-A17E-E511-9534-001E67A3EAB1.root' ] );


secFiles.extend( [
               ] )

