import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/864F0CD7-A90B-EA11-B25C-0025905B85D6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/D458DA6B-D20A-EA11-90F6-0025901D40A6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/0E1F53C3-5BF7-E911-911E-782BCB4FA8FB.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/1EBB1187-8CF7-E911-A2E0-0025905B8606.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3ED39766-58F7-E911-9B99-A4BF01158B40.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4619FD57-A9F7-E911-9AE3-002590DE6E32.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/46281CB1-3CFB-E911-A6D2-008CFA198314.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/48AD37DA-42F7-E911-BD4A-6CC2173C3E80.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4CB1BE01-5FF7-E911-AE63-FA163E3E5383.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/62A0622F-47F7-E911-924C-AC1F6B0DE2EA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6A9CB827-4FF7-E911-BC2F-0CC47AFF2472.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/82A95D39-4BF7-E911-AAFA-AC1F6B0DE362.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A8031807-43F7-E911-A395-44A842BE7718.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/CE3490B3-70F8-E911-8CA4-B026282986B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/DEE314F9-42F7-E911-AE76-90B11C070100.root',
] )
