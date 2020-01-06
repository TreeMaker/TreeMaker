import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/169A65EA-9B0E-EA11-89E7-0017A4770440.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/285A9335-9709-EA11-A522-1CB72C1B2D80.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/4A424124-7908-EA11-88A6-FA163EA17E34.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/6230B5C3-240C-EA11-A975-B083FED1321B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/A68073C0-3E0C-EA11-BA95-A0369FD0B198.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/BE1DB549-6C09-EA11-8DBE-002590494C84.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/CC87E305-7908-EA11-89B1-200009C4FE80.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/CE28BCA8-2709-EA11-8B96-008CFAFBDC0E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/F0043ACD-4A09-EA11-9F70-588A5AAEEBB8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/F656000B-6C09-EA11-AE0F-90B11C0BCDAD.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-750_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/FE8D8C2A-C00B-EA11-9AD5-0CC47A74525A.root',
] )
