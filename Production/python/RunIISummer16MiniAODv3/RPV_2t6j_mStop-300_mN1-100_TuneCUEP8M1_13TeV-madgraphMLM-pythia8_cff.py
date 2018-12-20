import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/0A131860-0FF3-E811-9846-0025904C540C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/1C3BE2FF-15F3-E811-AE3E-0CC47AFCC68A.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/281ACFBD-11F3-E811-8FC3-0025904C540C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/68579B77-09F3-E811-9319-0025905C95F8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/72B08C3D-1CF3-E811-A43D-0025904CF93E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/9C49F482-29F3-E811-983B-0CC47AFB7DA8.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/D255744E-05F3-E811-A723-0025905C975C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-300_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/80000/F22A5433-23F3-E811-A785-0025905C548A.root',
] )
