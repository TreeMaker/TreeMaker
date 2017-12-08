import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/0A5BC29C-BAF7-E611-885D-02163E01A231.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/22A12361-CDF7-E611-BECB-02163E019C5E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/267A867C-12F8-E611-BFA5-02163E013660.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/26866D5C-E0F7-E611-B632-02163E01A75D.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/60B0456B-6CF8-E611-88A5-02163E01A5D1.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C0E03EF3-14F8-E611-8038-02163E014418.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/DC391B97-01F8-E611-90CD-02163E019C89.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F6301D7D-17F8-E611-9CE8-02163E01A49D.root',
] )
