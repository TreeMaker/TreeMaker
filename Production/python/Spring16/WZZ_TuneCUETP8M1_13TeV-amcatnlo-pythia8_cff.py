import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/2427F776-D407-E611-A7DE-0090FAA573E0.root',
       '/store/mc/RunIISpring16MiniAODv1/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/40238A5D-D407-E611-AD66-00259073E3F2.root',
       '/store/mc/RunIISpring16MiniAODv1/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/5E04BB5A-D407-E611-A00B-0090FAA57C20.root',
       '/store/mc/RunIISpring16MiniAODv1/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/829D037D-D407-E611-8BD2-00259073E450.root',
       '/store/mc/RunIISpring16MiniAODv1/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/8A53FB5D-D407-E611-85B5-00259073E36E.root',
       '/store/mc/RunIISpring16MiniAODv1/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/60000/C45B3573-D407-E611-9DF2-005056021115.root',
] )
