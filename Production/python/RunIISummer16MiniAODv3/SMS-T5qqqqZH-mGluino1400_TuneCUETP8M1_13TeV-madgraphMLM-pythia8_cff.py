import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/16AF74B3-56EF-E811-A528-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/504F4276-64EF-E811-8C59-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/C0CBD884-55EF-E811-A55F-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/EC35AFD9-7AEF-E811-B96C-0242AC1C0501.root',
] )
