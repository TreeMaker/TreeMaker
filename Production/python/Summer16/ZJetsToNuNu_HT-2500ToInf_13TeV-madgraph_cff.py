import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0E1BD601-E5BD-E611-91B4-D8D385FF1940.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2EB4670C-25BF-E611-B9D4-90E2BACC5EEC.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/30A33F34-A8BE-E611-9350-0025905B861C.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/363FEF31-E6BD-E611-9410-90E2BACBAE58.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/58889015-A5BE-E611-89C2-0025905A48D0.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6CF7F2C3-24BF-E611-AA7D-0025905A60E4.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/904056B3-DEBD-E611-ACCE-0025905A607E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/96EAF1B6-0CBE-E611-8D8B-1CB72C1B63C2.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9CF41E57-DABD-E611-937C-0025905B859A.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BAE91920-DBBD-E611-B1AB-34E6D7E3878E.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DC5836B6-ECBD-E611-B280-1CB72C1B2D84.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EA37540D-EABD-E611-A6C9-1CB72C1B63C2.root',
] )
