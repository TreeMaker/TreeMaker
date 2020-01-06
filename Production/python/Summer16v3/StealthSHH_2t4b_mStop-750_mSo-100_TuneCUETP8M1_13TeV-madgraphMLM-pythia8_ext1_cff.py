import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/1018F26D-3A06-EA11-A60D-002590908286.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/1E2C789B-4B06-EA11-98D1-A0369FD0B266.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/2ACE5CF4-3206-EA11-B0F8-801844E561B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/34C7F3BA-9006-EA11-A5BC-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/3A01E2F7-3906-EA11-827E-0CC47AFF0168.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/42DE680B-6506-EA11-B18A-3417EBE2F0B2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/7C07A7BE-3306-EA11-B3AE-001E67E6F8B4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/90975397-9A07-EA11-9A34-0CC47A5FBE31.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C8152D32-5306-EA11-B3CB-0CC47AACFCDE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/CE1B9ED5-AF06-EA11-ADE1-FA163E751994.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/CEBD4A28-3706-EA11-AC0D-E0071B7A4550.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/D271CFBF-7606-EA11-A8ED-1866DA7F9349.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/E8A17D47-A506-EA11-8273-F4E9D4AF1010.root',
] )
