import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/1010000/40A07F6B-191B-EA11-B712-AC1F6B0F6FCE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/04895EA2-1912-EA11-9BC9-1866DAEA79D0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/10AF9BCB-1212-EA11-87CF-002590D8C724.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/1C9E7688-1612-EA11-8A43-B496910A868C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/3A802247-1A12-EA11-BFED-0242AC1C0503.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/3EB60DF7-4511-EA11-9318-0025905C3D40.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/4A9424B6-1B12-EA11-BCE3-AC1F6BC67D48.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/52F76202-1712-EA11-8200-5065F3818291.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/5A2665DD-1112-EA11-83AE-001E67A3AEB8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/6EBE5A20-2812-EA11-9EF5-44A842482557.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/8212C0CA-1412-EA11-A2A2-7CD30AB190AE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/867484B8-4811-EA11-9972-FA163EE0EB8B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/90990CB8-1312-EA11-BA91-BC305B3909FE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/94BD59F7-1D12-EA11-8B2C-44A842B4CC98.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/A0C61585-1E12-EA11-AE82-0CC47A7E6A4C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/A2CCAD7A-1A12-EA11-B988-003048CB7DA2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/A81A7600-4711-EA11-812F-0025905B8612.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/AEED7125-2E12-EA11-9C0F-0CC47AD98D08.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C689A24A-2E12-EA11-BE23-A4BF01125548.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/CCCC0CE0-1712-EA11-8A74-6CC2173D5F20.root',
] )
