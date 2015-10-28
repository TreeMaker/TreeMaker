import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/10000/2433FFC7-C877-E511-9976-001E67A3EF48.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/10000/60ABBAE2-CA77-E511-A091-90B11C064B50.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/10000/6E4F83C9-C877-E511-8B2D-90B11C064B50.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/10000/8C4B3221-CB77-E511-A740-001E67A42026.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/10000/9A8F76EA-CA77-E511-8EDC-90B11C064AD8.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/10000/AAC0148D-CB77-E511-8EE0-001E67A42175.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/40000/4E4CFF42-C977-E511-9FA8-001E67A400F0.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/40000/7232AC45-C977-E511-9C2F-D4AE529D9537.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/40000/9870CF40-C977-E511-B642-001E67A4061D.root',
       '/store/mc/RunIISpring15MiniAODv2/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v2/40000/F0D8C552-C977-E511-A965-001E67586629.root' ] );


secFiles.extend( [
               ] )

