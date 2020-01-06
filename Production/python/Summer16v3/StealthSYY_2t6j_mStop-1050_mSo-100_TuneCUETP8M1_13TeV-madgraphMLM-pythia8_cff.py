import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/1A939FCB-5005-EA11-9349-246E96D14C78.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/20876246-5005-EA11-BA4F-0025905C431C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/20A70D9B-D005-EA11-B2BE-7CD30AD0A72C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/4E998A4E-8A05-EA11-9641-0CC47AD98CF0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/6687E75C-5005-EA11-85B2-FA163EF329D4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/84A28E2D-8B05-EA11-BB24-002590DE6E5E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/96413B4C-5005-EA11-B2A4-A0369FE2C1E8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/9EBF6EEC-5005-EA11-BB70-E0071B7A6850.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/B028BF70-5105-EA11-9056-002590DC03C6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/C605D072-C305-EA11-9205-A0369FF88214.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/C819D851-8A05-EA11-9F6A-0025905A60B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/D487939F-DE05-EA11-AAC9-0CC47A5FBE25.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1050_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/EA8D5359-8A05-EA11-BE1E-AC1F6B0F3A26.root',
] )
