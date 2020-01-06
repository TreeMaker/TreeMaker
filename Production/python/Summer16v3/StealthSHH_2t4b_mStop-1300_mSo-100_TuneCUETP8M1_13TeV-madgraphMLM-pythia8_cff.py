import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/04E48DE4-17F7-E911-8ABC-0CC47AD98F74.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2006BF08-1BF7-E911-8914-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2A7B4179-E8FD-E911-8BE9-0CC47A78A456.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/2AAF91CE-1AF7-E911-8448-AC1F6B0DE4A2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/38BC6A18-B9F7-E911-BF2C-509A4C78138B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5085E9FF-26F7-E911-BB66-0CC47A5FC2A1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5E0572FC-22F7-E911-B813-0CC47AFF0480.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/683268E4-17F7-E911-A20B-E0071B73B6D0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6A9DE0F5-3EF7-E911-AB8C-001E67A3EF70.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/6EC84B94-47F7-E911-8997-FA163E2A4519.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/8A7999E4-27F7-E911-8777-0242AC1C050A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9C380ED4-1AF7-E911-A1D6-7CD30ACE23E6.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/AE6A7B27-1BF7-E911-A59B-7CD30AC030F8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B6C05A29-3BF7-E911-AAAB-0CC47A1E0466.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/BA58A385-37FB-E911-95F8-B496910A0290.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/C8A41B9E-28F7-E911-83C2-00259075D708.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/CE07B23C-E8FD-E911-9837-002590DE6C96.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D4D26DBF-2FF7-E911-8805-20040FE9CF38.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D4D963F3-26F7-E911-B347-D48564591B68.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D68A15D2-1AF7-E911-875F-008CFAF558E0.root',
] )
