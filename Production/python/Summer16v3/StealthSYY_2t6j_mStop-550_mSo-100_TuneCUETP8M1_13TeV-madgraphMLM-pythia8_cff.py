import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/00FE985B-58F6-E911-AB45-0CC47AA989C0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/20443F62-59F6-E911-968B-0CC47A5FC285.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/260F7CE9-5AF6-E911-86E3-B499BAAC3786.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2A29F75C-58F6-E911-B5AE-001E67A3EBD8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3A3169E2-57F6-E911-A803-24BE05C3CBD1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/4897E9B2-F2F5-E911-9773-FA163E08AD45.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/48C8D5AB-59F6-E911-9220-7CD30AD097C0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/506358FF-58F6-E911-8D0E-38EAA78D8B54.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5C71F51A-59F6-E911-B495-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5EDE173A-58F6-E911-B242-405CFDFF481B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/608FA0C6-58F6-E911-AE47-AC1F6B0DE45C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/642AEAFB-58F6-E911-9027-BC305B390A4C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8A03E0B6-58F6-E911-8638-0CC47AFCC6EE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8E4A2409-59F6-E911-A7B2-7CD30AD08ED2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9ACAAE29-59F6-E911-818E-002590791DA2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/A647CCD8-58F6-E911-A3D5-0CC47A78A3EC.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B6ECE88D-59F6-E911-9F06-AC1F6B56762A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C62714AA-58F6-E911-ACD0-246E96D14E34.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D2C725FB-58F6-E911-9EDE-F4E9D4A37DB0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-550_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/FC036D9E-58F6-E911-B072-0242AC130002.root',
] )
