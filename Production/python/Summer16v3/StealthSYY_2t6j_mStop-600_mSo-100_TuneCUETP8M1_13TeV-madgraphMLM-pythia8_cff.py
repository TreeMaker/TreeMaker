import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/00FA3481-63FB-E911-8364-44A842B4D8D8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/12272C07-61FB-E911-8796-AC1F6B1AEFFC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/124E1010-61FB-E911-9F31-0CC47A6C063E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/14575E07-61FB-E911-8C99-EC0D9A0B3350.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/20A32B54-7FFC-E911-909F-509A4C74D082.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/34184206-61FB-E911-AEBF-001E6779261A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/5C177907-61FB-E911-B681-48FD8EE73989.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/765E6684-63FB-E911-A6F8-0CC47A5FC679.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/90C45CA3-F6FA-E911-B9D7-FA163E890248.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/92B74104-61FB-E911-836E-002590909282.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/983FAA1B-62FB-E911-9015-EC0D9A822636.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/AC1C5C06-61FB-E911-9598-0CC47AFF02AC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/DC518BBE-64FB-E911-9DCE-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/E6E0ADFB-61FB-E911-8F58-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-600_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/F004C93A-61FB-E911-A1FF-44A842CFD5BE.root',
] )
