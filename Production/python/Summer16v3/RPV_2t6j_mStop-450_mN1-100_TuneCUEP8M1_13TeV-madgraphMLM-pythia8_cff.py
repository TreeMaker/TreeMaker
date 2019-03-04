import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/16274DAD-ABF0-E811-A116-001CC4A6DC78.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/8ADE28C0-B4F0-E811-A3E8-0025905B8598.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/8C018F54-BDF0-E811-ABBC-003048FFD75A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/AE63F7C6-08F1-E811-B0F0-484D7E8DF114.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/BC6230D4-ABF0-E811-93C6-0025905A6118.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/EA92461E-C5F0-E811-B5F0-0CC47A7452D0.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-450_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/FE24333B-CAF0-E811-92E9-0025905B858A.root',
] )
