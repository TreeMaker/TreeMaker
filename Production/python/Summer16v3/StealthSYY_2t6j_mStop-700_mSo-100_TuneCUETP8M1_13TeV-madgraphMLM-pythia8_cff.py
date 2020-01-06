import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/06D6E977-61F7-E911-92B7-0025901D40D0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/12213193-61F7-E911-83DD-5065F38102F1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/1EA3B571-61F7-E911-A0A3-F4E9D4AEC940.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/3A5A941A-61F7-E911-A8C0-6CC2173C3DD0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/3EDDA85B-61F7-E911-BBC3-001E67D80528.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/4AAE562B-61F7-E911-819A-002590D60000.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/800EBDFC-60F7-E911-A663-44A842CFD5BE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/84AD7771-61F7-E911-98F9-0025909077C6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/C423F673-61F7-E911-BB72-FA163EA0CC31.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/E866E25C-61F7-E911-8081-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-700_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/FC409006-62F7-E911-800C-002590791DA2.root',
] )
