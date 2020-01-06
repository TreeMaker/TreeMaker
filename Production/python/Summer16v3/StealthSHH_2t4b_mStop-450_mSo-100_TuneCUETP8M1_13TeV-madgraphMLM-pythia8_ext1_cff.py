import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/0AA87908-1BF7-E911-B06C-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/10C0D4A9-37F7-E911-9E66-002590DD61E0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/144EF3E9-C9F6-E911-AD22-AC1F6B0DE0A0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/1A3D9E1C-8DF7-E911-9280-00259090785A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/1AA93FE2-A0F7-E911-AFB9-509A4C748057.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/20BC1CD6-DAF6-E911-B1DE-D48564592B02.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/36C704B7-D7F6-E911-94FD-44A842CFC9CC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/4821E87E-D4F6-E911-9B65-AC1F6B0DE45C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/48DC3E98-59F6-E911-8EF6-FA163E4880F3.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/4C361BCE-D4F6-E911-AC64-F04DA27540BB.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/58684420-D5F6-E911-9211-E0071B7A8560.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/5ABA21FF-D8F6-E911-AF7F-7CD30ACE23E6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/66F66984-37FB-E911-B531-B496910A0290.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/6A0120DC-8CF7-E911-B0DC-0025905A48F0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/7EB92E95-CCF6-E911-8E0D-14DDA924324B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/8276FF47-CEF6-E911-8806-509A4C9F8A8E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/868A8966-58F7-E911-B599-A4BF0115A300.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/92AAEA75-D5F6-E911-8015-0025901F8740.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/A2E275B9-D7F6-E911-9548-28924A33B9AA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/A87F7212-D5F6-E911-9D01-001E675A6AA9.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/AEAD5845-CEF6-E911-9F6E-0025901D4446.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/B6A16FEA-D4F6-E911-97B9-0CC47AFF0470.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/BA978C15-CFF6-E911-835D-C4346BC85718.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/C67839E9-CAF6-E911-8515-00269E95ACE4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/C8EEEA52-CEF6-E911-B124-90B11C2C93B1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-450_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/F4955B46-CEF6-E911-93FD-20040FE9C81C.root',
] )
