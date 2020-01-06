import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/260000/4494B752-7F1B-EA11-88E4-6CC2173D5F20.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/260000/50869C80-5A1B-EA11-8AB6-AC1F6B0F75D4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/260000/EE98EE85-7F1B-EA11-B781-A4BF01013F29.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/260000/F6907D88-7F1B-EA11-BA22-001EC94B4429.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/2610000/0E9C7CF3-151B-EA11-9440-48FD8EE73ACD.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/082C4239-AD11-EA11-B616-FA163EF5080B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/14E51C0B-AA11-EA11-A017-782BCB4FBC9F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/405D4789-4D12-EA11-A590-001E67792808.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/4620C74D-5912-EA11-B5DD-AC1F6B8DD22E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/50132982-B612-EA11-B910-7CD30ACE1750.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/560AAF97-5512-EA11-80ED-0CC47AFF23E6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/568180A4-4612-EA11-9277-246E96D14C70.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/5E574D69-7212-EA11-BEE9-047D7B2E81BC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/6A5C7756-4A12-EA11-8970-801844E55BCC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/6C12780F-4212-EA11-A6F4-002590DE6E22.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/78BE5152-4A12-EA11-A211-001E67DDC254.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/7CF67A1F-4F12-EA11-AE7B-003048CB87DE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/8CAC64EF-4C12-EA11-92C9-0CC47AD99146.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/9ABC2737-4712-EA11-BB77-3417EBE520A5.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/A4F311DA-4B12-EA11-A79B-98039BA0B4FA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/B20DFA6A-5012-EA11-8434-3CFDFE55F2C2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C0A79C6F-5112-EA11-B04D-0CC47A4D7626.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C4499864-5112-EA11-A90C-1CC1DE048FB8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/C6F1A456-4912-EA11-88D3-008CFAC94130.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/DA7CA481-4D12-EA11-828C-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/EA0CDDEC-5412-EA11-918D-00259094F2BF.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/F0795B4A-5112-EA11-9E4D-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-400_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/30000/F4582C92-6412-EA11-95F4-7CD30AC030B4.root',
] )
