import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/2635556F-500C-E611-B4BD-002590D9D968.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/74641F0C-620C-E611-BD91-0025907859B4.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/805611CD-1A0C-E611-A684-0CC47A0AD6E4.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/30000/8AA8B02B-200C-E611-8A63-00304867FD43.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/20FE03C5-2F06-E611-A5E4-008CFA50268E.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/2A0F081E-C106-E611-96A5-0CC47A0AD742.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/681497B0-C006-E611-A071-001517FBE024.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/6A2F6450-6E06-E611-B951-008CFA197AF4.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/846D22BD-F005-E611-9875-0002C94D5504.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/ACB7E5BC-9805-E611-B18C-001E67A401B3.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/B49C6F95-3807-E611-84EF-44A84224BE51.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/C4090DA6-F005-E611-B31B-002590D9D8B6.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/F022E9B3-C006-E611-9F7F-90B11C2CC96F.root',
       '/store/mc/RunIISpring16MiniAODv1/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/50000/FA19F65E-3006-E611-BB8B-90B11C06954E.root',
] )
