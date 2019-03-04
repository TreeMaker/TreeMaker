import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/1AF9F07D-48F0-E811-A944-B083FED3F4E2.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/32176BA7-5AF0-E811-A033-20040FE9DE50.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/40C9FA32-43F0-E811-98A9-1866DAEB40CC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/9693B531-5FF0-E811-9B38-20040FE94274.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/9E9EFE97-47F0-E811-A5A8-782BCB537DB9.root',
] )
