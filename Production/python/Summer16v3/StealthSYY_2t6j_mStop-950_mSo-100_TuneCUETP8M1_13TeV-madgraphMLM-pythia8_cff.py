import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/0C67EDCC-31FB-E911-8A6D-002590FD5E70.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/14118F13-33FB-E911-A55A-B026282956A0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/246174ED-31FB-E911-B8EF-00259090832A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/28E129CD-31FB-E911-8457-0CC47A706D26.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/2E73EDDF-31FB-E911-AB91-6CC2173C4580.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/561F63EF-32FB-E911-AD19-B496910A9A30.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/74C150BF-32FB-E911-9B2D-AC1F6B0DE2FA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/AAB25B56-32FB-E911-BC7D-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/AAD70FE9-F2FB-E911-A202-0CC47A7C3422.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/BEFF26E4-31FB-E911-8072-A4BF0108B7E2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/C4B5ABD5-31FB-E911-A0FD-48FD8EE73A73.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/C6AE17AF-32FB-E911-B46E-FA163E565520.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/DE94A9A1-32FB-E911-9B3A-0CC47AD99062.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-950_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/E0DC1CB0-3EFB-E911-8B43-0CC47AFCC3AA.root',
] )
