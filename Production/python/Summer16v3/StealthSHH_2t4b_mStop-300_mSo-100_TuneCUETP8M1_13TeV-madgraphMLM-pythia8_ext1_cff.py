import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/00FC0091-790C-EA11-937D-3417EBE6459A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/04486D83-7908-EA11-A322-0025905C42F4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/2A92B6F6-2F0C-EA11-8A10-BC305B3909FE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/4413685E-740E-EA11-8DB2-AC1F6B1AF194.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/48BAFEA5-2709-EA11-9D48-509A4C74D1B3.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/5ADA4544-F50A-EA11-BF45-0CC47A7C340C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/682955DE-610B-EA11-8708-AC1F6B0DE13A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/78A5DC58-DC07-EA11-897F-FA163E99BEF2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/8808430F-4B09-EA11-9F30-008CFAC94004.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/907ABEF0-300B-EA11-8E70-A0369FC5DCB8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/92345305-A80B-EA11-84EF-0017A4770460.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/926C4405-260A-EA11-8C43-38EAA78E2C94.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/9C690CE3-B009-EA11-8271-20040FF49604.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/AC50C8D3-1D0D-EA11-9824-20CF305B066E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/B6AF0578-2209-EA11-BEA4-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/C89041F0-6B09-EA11-B5EF-0CC47A2AED04.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/CAC7A853-9B08-EA11-A6DE-003048F2E65E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/DE4524F5-240C-EA11-9224-002590D600EE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/EA9F4F90-3A0B-EA11-9CE9-001E67A3E8CC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/F62B7C64-BD08-EA11-A8EF-0CC47A57CD00.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/FAE43359-6C09-EA11-920A-A4BF012881D0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/FE801607-7908-EA11-B61C-24BE05C626C1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/40000/FEDFC337-F508-EA11-B248-7CD30AC0301A.root',
] )
