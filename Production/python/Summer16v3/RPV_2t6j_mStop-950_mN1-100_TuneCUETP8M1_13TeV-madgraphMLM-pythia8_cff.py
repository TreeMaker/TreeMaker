import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/10C28465-43F6-E911-B1A2-0CC47A4DEE6E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/1268F21D-43F6-E911-9A7D-34800D4F9650.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2C68124D-43F6-E911-9891-0CC47A2B0906.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/36611B2C-44F6-E911-BE52-FA163E584F44.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/36AA4802-43F6-E911-A02B-008CFAFBE70C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/62373C1E-43F6-E911-BD0F-246E96D149DC.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6E3ADE49-43F6-E911-9974-5065F381D2C1.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8CA5241B-43F6-E911-8C8E-7CD30AC0370E.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9005AD10-43F6-E911-B3BE-0CC47A7C354C.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E4656611-43F6-E911-9F7B-1CB72C1B6574.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-950_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E861AE64-43F6-E911-92B0-0CC47AFF04B0.root',
] )
