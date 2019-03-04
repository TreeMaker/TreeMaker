import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/080AAD63-A8EF-E811-B378-1866DA87AFB4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/1AB6F05B-81EF-E811-8771-1866DA87A7E7.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/1AEFFC14-8DEF-E811-89CC-D4AE526A0922.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/904E9F15-7EEF-E811-9CF2-1866DA87A870.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/98AE1EC4-60EF-E811-8C28-0CC47A00934A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/C698F1A5-75EF-E811-B4D8-1866DA86CCDF.root',
] )
