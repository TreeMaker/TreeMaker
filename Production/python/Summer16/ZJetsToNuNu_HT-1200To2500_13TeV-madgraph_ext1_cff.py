import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/48943867-7EC2-E611-ADD0-0CC47A13CB62.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/747C9166-94C2-E611-ABA6-0CC47AD98B94.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/76BB4013-89C2-E611-90EE-0CC47AD98CF0.root',
] )
