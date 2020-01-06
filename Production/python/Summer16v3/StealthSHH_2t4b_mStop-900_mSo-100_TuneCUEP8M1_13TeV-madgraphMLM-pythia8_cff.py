import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/108A75FB-58F6-E911-BA8A-F4E9D4AEC940.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/168809A5-58F6-E911-B7B8-0CC47A4D761A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/1C68260B-59F6-E911-96CD-3417EBE2F0DF.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/34AD01B5-58F6-E911-8080-0CC47AFCC69A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/488B7977-59F6-E911-911A-0CC47A5FC619.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5E4511E8-58F6-E911-AC60-AC1F6B0DE348.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6C1E5283-59F6-E911-8EA2-7CD30AD097C0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/742115D9-58F6-E911-9633-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C06CA5AC-58F6-E911-81F8-0CC47AFC3C76.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C287AA02-59F6-E911-B8FB-FA163EBB7F4F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-900_mSo-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/F6836734-58F6-E911-925A-7CD30AC031E8.root',
] )
