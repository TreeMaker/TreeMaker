import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/005553E6-18F5-E811-987E-AC1F6B0DE33A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/16552BCB-3BF5-E811-B7EA-AC1F6B0DE4A8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/2861C8DD-3BF5-E811-BB20-48FD8E2824B3.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/3C221133-1EF5-E811-89C6-A0369FD0B32E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/4E82AEF9-1FF5-E811-ACB2-AC1F6B0DE490.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/68FB9D67-20F5-E811-9090-A0369FD0B15C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B8A3B4F6-27F5-E811-BAA3-A0369FE2C132.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-400_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/C68E4D36-83F5-E811-A53A-AC1F6B0DE4A8.root',
] )
