import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/08B200DF-3107-EA11-BD4E-3417EBE527D4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/0EC065BE-DA05-EA11-9D31-EC0D9A82264E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/28FEF6AE-D305-EA11-B898-0CC47A7C34C8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/2AE9DFC0-F005-EA11-BAFE-A0369FE2C044.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/3A6176F2-F005-EA11-9632-44A842CFC971.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/46DFD2A6-6406-EA11-882C-C45444922B77.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/4884DAC4-ED05-EA11-87A6-20040FF477F8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/7869ABFD-E205-EA11-8C06-002590907856.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/7C40A998-D305-EA11-8C50-D4AE5290244F.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/C8888AFA-6406-EA11-BDA2-AC1F6B1B2364.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/CEAEBE4F-A506-EA11-957F-20CF305B05BE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/E0D2F419-D405-EA11-A52E-0CC47AFCC6A6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/F46FE731-CD05-EA11-84DA-509A4C748A1D.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/30000/FCAAD684-FC05-EA11-8EDC-002590D9D8AC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/CC558171-2D09-EA11-86E6-1866DA8F75C0.root',
] )
