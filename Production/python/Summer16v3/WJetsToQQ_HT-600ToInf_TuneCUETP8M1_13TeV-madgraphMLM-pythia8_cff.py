import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/0EFB560B-37F0-E811-9540-842B2B42B758.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/2034FD91-37F0-E811-B654-A4BADB22A4AC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/22C9FD9E-38F0-E811-A118-A4BADB22A4AC.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/46962411-36F0-E811-B6D1-001EC94B4EF3.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/849FF9AE-C5F1-E811-8655-1866DAEA79A4.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/ACAFBB06-39F0-E811-A6A3-801844DEF068.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/EA29EF2A-78F1-E811-8385-1866DAEA79D4.root',
       '/store/mc/RunIISummer16MiniAODv3/WJetsToQQ_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/F2BC84F6-36F0-E811-AC3F-B083FED3EE24.root',
] )
