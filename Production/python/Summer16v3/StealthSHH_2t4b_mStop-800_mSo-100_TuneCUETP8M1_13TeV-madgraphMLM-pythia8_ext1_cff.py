import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/44558A1F-80F6-E911-989A-0025900E3502.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/5C9CD5D5-7EF6-E911-93C0-44A842BE76F1.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/8A0C5647-80F6-E911-BF72-FA163E7ED2D2.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/94D1E632-80F6-E911-8DA0-008CFAF71666.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/A28EFC4C-80F6-E911-B944-002590909086.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/A60D2F38-80F6-E911-AFD6-0CC47AFF0218.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/A66D70D2-80F6-E911-BA03-0025905B85E8.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/CED3CB8F-7FF6-E911-95FE-0CC47A7E68AA.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/EE46AD33-80F6-E911-9C2A-AC1F6B0DE3EE.root',
       '/store/mc/RunIISummer16MiniAODv3/StealthSHH_2t4b_mStop-800_mSo-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/60000/F4AEA34C-80F6-E911-85D4-0242AC1C0502.root',
] )
