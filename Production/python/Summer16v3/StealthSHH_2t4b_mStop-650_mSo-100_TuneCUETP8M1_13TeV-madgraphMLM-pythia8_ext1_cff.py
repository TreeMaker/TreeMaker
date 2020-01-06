import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/165EF9C2-65F6-E911-9E25-0025905D1E0A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/200F57CD-65F6-E911-AAC7-6CC2173C3DD0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/26860E4E-65F6-E911-8584-EC0D9A8221CE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/5077E8CB-65F6-E911-BB34-A4BF01283D2E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/60B969D5-65F6-E911-A69A-10983627C3DB.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/72A68EC5-65F6-E911-A540-0090FAA58564.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/9E04BB77-66F6-E911-84F8-001E67D80528.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/A051E3C9-65F6-E911-87F4-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/BA3374F6-65F6-E911-ABF8-509A4C749119.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/BE7128D3-65F6-E911-9FF9-B026282986B0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/CE90FD69-66F6-E911-8285-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/D4401BAB-65F6-E911-AE44-0CC47AD99044.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/D8E0E2DF-65F6-E911-A9BE-44A842CFD5B1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-650_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/E201E3D2-65F6-E911-AE1B-6C2B59900458.root',
] )
