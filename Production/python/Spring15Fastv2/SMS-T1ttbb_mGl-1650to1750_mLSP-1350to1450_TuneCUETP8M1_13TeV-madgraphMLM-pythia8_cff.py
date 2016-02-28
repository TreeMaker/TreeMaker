import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/2E6252EF-44D4-E511-A185-D8D385FF3339.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/30BCD25D-45D4-E511-B0A4-6CC2173DBFB0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/36E7A108-45D4-E511-8E7E-6CC2173DC2E0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/38F453F2-44D4-E511-B312-D8D385FF344D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3C7FE210-45D4-E511-806F-002590DE6E34.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3E295146-45D4-E511-AA54-6CC2173DBF20.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/3EB58409-45D4-E511-B7DF-6CC2173D93F0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/42CCE140-45D4-E511-8633-6CC2173D9AD0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/50DC0FE1-44D4-E511-9637-002590DD7C9E.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/5ABA33DF-44D4-E511-985C-3417EBE7062D.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/765F59EE-44D4-E511-8A6C-0025B3E05BE9.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/866343E6-44D4-E511-A847-D8D385FF340B.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/941E6F87-45D4-E511-85EE-3417EBE743C0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/96909DE0-44D4-E511-9866-3417EBE74303.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/9A827D14-45D4-E511-BED8-0024E85A3F75.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/A4766808-45D4-E511-8482-6CC2173DABE0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/C8DED14E-45D4-E511-ADCB-6CC2173DBEE0.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1ttbb_mGl-1650to1750_mLSP-1350to1450_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/60000/EACCEFDF-44D4-E511-B5EC-3417EBE7047A.root',
] )
