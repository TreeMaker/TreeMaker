import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/005CE95F-1900-EA11-9364-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/0E8B1F84-5900-EA11-B36F-C45444922D6C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/3A8C64E7-1A00-EA11-9E5D-0025904A8EC8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/42A2EE5F-FFFF-E911-84A3-E0071B73C650.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/4C3A965A-5B00-EA11-A04B-0CC47A5FC679.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/5C7B654E-1A00-EA11-9937-509A4C748085.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/6A6AF366-2100-EA11-9DF9-FA163E4A2D4B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/900C0EFE-7900-EA11-BBFB-AC1F6B0DE294.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/9493B189-AB00-EA11-B8AF-0242AC1C0505.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/A0EABB1B-2A00-EA11-976D-44A84225C7BB.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/A2684481-4D00-EA11-A605-0CC47A7C3444.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/BAD18D46-FAFF-E911-8201-20040FE8E914.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/C470A341-0E00-EA11-9166-A0369FC5B844.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/D26B3E00-2E00-EA11-AFB5-509A4C85407E.root',
] )
