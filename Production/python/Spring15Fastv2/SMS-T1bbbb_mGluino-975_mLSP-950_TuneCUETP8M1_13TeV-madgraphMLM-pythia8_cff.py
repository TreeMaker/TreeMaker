import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/283A3D3B-957B-E511-9782-02163E00C04A.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/B0A46810-567C-E511-885C-001E67E71D03.root',
       '/store/mc/RunIISpring15MiniAODv2/SMS-T1bbbb_mGluino-975_mLSP-950_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/FastAsympt25ns_74X_mcRun2_asymptotic_v2-v1/80000/C496B9CA-957B-E511-B137-02163E015CC9.root' ] );


secFiles.extend( [
               ] )

