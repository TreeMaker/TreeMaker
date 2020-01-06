import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/06C6315B-9E0D-EA11-B195-AC1F6B1AF1B4.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/0EA6258C-6E0D-EA11-9C97-0CC47A7E6A6C.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/24FB2690-800D-EA11-ACCC-B026283465C0.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/5E978ED1-920D-EA11-834C-B49691408AFE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/60682AFA-8C0D-EA11-BDCE-B4969109FE30.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/66A02B70-6E0D-EA11-9F07-AC1F6B56762A.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/6A1C47AD-C30C-EA11-8356-FA163EF1373E.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/7A50587A-9B0D-EA11-9BAF-6C2B5990D12B.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/9CE6E99A-7C0D-EA11-B2A0-002590907772.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/ACB9E1DF-700D-EA11-8280-0025905C5500.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/B017D313-9E0D-EA11-9E6B-AC1F6B0DE338.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/20000/EE421253-6B0D-EA11-8B78-24BE05BD4F61.root',
] )
