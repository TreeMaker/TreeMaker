import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/0ADE73A8-637E-E511-BC84-008CFA052194.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/16CBCBA2-637E-E511-987D-00266CF9AB9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/24A6F1A2-637E-E511-9463-008CFA152144.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/4EE8669E-637E-E511-A619-549F35AD8BC9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/60F05DB0-637E-E511-8E72-008CFA0647D8.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/66818DA8-637E-E511-8697-008CFA052194.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/6A567CA4-637E-E511-A6F6-008CFA0A5818.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/70D5FDA2-637E-E511-BD04-00266CF9B828.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/7415419E-637E-E511-ACD9-549F358EB762.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/940D89A2-637E-E511-9E04-00266CF9B5D0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/CA1996A8-637E-E511-9C50-008CFA052194.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D839CDA2-637E-E511-BDE6-00266CF9AB9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/D889F0A2-637E-E511-8C04-00266CF9AB9C.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1tttt_mGluino-775_mLSP-475to550_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/ECFBB0A2-637E-E511-BFE8-00266CF9B828.root' ] );


secFiles.extend( [
               ] )

