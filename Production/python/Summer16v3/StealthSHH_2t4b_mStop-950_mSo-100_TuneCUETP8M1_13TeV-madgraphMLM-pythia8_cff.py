import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/6ED24E8F-3A0B-EA11-864A-001E67DDC24A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/A230C85A-A807-EA11-B9AB-FA163E08864D.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/A27A812C-2209-EA11-8D7A-0242AC1C050F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/E06C49D1-4B0B-EA11-90B7-0CC47A78A360.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/F4101609-4B09-EA11-89E9-008CFAC94008.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/40000/FE6C717E-7908-EA11-A794-0025905C3E66.root',
] )
