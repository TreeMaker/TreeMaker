import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/1A55ABC1-12EA-E811-8C63-002590D601B8.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/76974E96-15EA-E811-BAC6-1418776420DF.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/7885258D-11EA-E811-AE26-44A84225C851.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/7C8A347B-15EA-E811-BDA4-14187764197C.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/82643C35-BEEA-E811-AAAB-B083FED138B3.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/9AC929A0-11EA-E811-8635-002590D8C71A.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/D8B36EA0-12EA-E811-A062-0CC47AFC3C80.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/F063F716-14EA-E811-8FA7-44A842240F8D.root',
       '/store/mc/RunIISummer16MiniAODv3/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/110000/F8ABC0B5-10EA-E811-948B-14187763B811.root',
] )
