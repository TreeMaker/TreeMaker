import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/065D3D09-CA6D-E511-A59C-D4AE526A0461.root',
       '/store/mc/RunIISpring15MiniAODv2/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/20FF3B81-C96D-E511-AAB8-441EA17344AC.root',
       '/store/mc/RunIISpring15MiniAODv2/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/2EF6C807-CA6D-E511-A9EE-842B2B758AD8.root',
       '/store/mc/RunIISpring15MiniAODv2/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/30FDAF08-CA6D-E511-828C-D4AE526A0C7A.root',
       '/store/mc/RunIISpring15MiniAODv2/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/4A1B071A-CA6D-E511-8D8E-441EA1733FD6.root',
       '/store/mc/RunIISpring15MiniAODv2/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/90D98A05-CA6D-E511-B721-00266CFFBDB4.root',
       '/store/mc/RunIISpring15MiniAODv2/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/A8935398-C96D-E511-86FA-1CC1DE18CFF0.root',
       '/store/mc/RunIISpring15MiniAODv2/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/60000/E80D9307-CA6D-E511-A3A7-003048FFCB96.root' ] );


secFiles.extend( [
               ] )

