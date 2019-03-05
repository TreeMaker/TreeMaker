import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/1C374D9B-FCF0-E811-BE41-001E67D8A423.root',
       '/store/mc/RunIISummer16MiniAODv3/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/2ADC6EC7-32F1-E811-BAA1-001E67586629.root',
       '/store/mc/RunIISummer16MiniAODv3/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/5C16F743-26F1-E811-BE31-0026182FD776.root',
       '/store/mc/RunIISummer16MiniAODv3/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/90CF0E54-C5F1-E811-818E-EC0D9A0B30D0.root',
] )
