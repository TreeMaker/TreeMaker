import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/0E3A894A-69EF-E811-86CC-0CC47A7C345E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/1238BA7F-DDEF-E811-881D-0025905A613C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/747690FC-85EF-E811-9B41-0CC47A4D7634.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/74DD9278-69EF-E811-82BB-0CC47A78A360.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/AC1B1553-69EF-E811-B7EB-0CC47A4C8ECA.root',
] )
