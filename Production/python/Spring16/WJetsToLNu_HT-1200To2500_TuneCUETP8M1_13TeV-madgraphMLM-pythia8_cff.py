import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/06951851-69FA-E511-9B79-0025905C3E66.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/629E5356-69FA-E511-9E7D-0025905C3E68.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/74DF9D54-69FA-E511-AC89-0025904CF710.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/B8EE3055-69FA-E511-804F-0025905C4264.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/BEF98652-69FA-E511-ACA9-0025904C66A6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/D4C2AA4F-69FA-E511-84CE-0025905C2CBC.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/40000/D8DC140E-69FA-E511-8EDA-002590FD5694.root',
] )
