import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/3A2285C7-CA6D-E511-B68F-0CC47A13D09C.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/82196D81-CB6D-E511-9C59-0CC47A13D2BE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AC8AA3D3-CA6D-E511-81F2-002590E39D90.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E23816C8-CA6D-E511-97A4-002590E2F664.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/34A1F0E2-CA6D-E511-8E3E-0025905C2C84.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/40000/3C7038E2-CA6D-E511-8553-0025905C3DCE.root',
       '/store/mc/RunIISpring15MiniAODv2/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/50000/6CD88A88-CB6D-E511-919E-0025904C540E.root' ] );


secFiles.extend( [
               ] )

