import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3A79A4D6-F2B9-E611-89C5-842B2B42BED6.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3E0C60AF-EFB9-E611-A6C1-B083FED424C4.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/48E050F4-F4B9-E611-BFAB-24BE05CE2EE1.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/623F951B-01BA-E611-AB9A-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/82F66E3B-F9B9-E611-A1A1-1866DAEA6D08.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D6CCF931-FDB9-E611-95D5-001EC94BFB16.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E82D791D-F7B9-E611-9F62-782BCB539B16.root',
       '/store/mc/RunIISummer16MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FEB6C285-00BA-E611-9EBC-842B2B42B75A.root',
] )
