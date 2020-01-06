import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/340DF284-CFFA-E911-986B-F01FAFD9CC64.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/4033B4B6-EBF9-E911-BA87-FA163E2E1AF6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/52DFBE1B-C7FA-E911-ADCB-0CC47AD98CEA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/A8FF6FA5-C0FA-E911-9AF3-B8CA3A70A520.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/BAD56356-C0FA-E911-B3A4-AC1F6B0DE224.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/E23A9A0E-D6FA-E911-8D2C-0CC47AFF0448.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/E83A7535-F6FA-E911-8F6F-0242AC1C0506.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/F6E7257A-D2FA-E911-A92A-0CC47A5FC2A5.root',
] )
