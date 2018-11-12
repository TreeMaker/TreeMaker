import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/728021A3-EAFC-E611-A0E3-02163E0120DA.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/40CB68F8-9EF7-E611-A50E-02163E014648.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/54F6D68D-01F8-E611-9FC4-02163E01356E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/7A2149EB-08F8-E611-A980-02163E014226.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/8A34C0D5-A7F7-E611-83F3-02163E01A1FC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A8C95A30-DBF8-E611-BEE5-02163E019E12.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AC918DF4-A0F7-E611-BD50-02163E019B80.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E66A0EA8-EAF7-E611-A2FA-02163E019D95.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/EC618218-FBF6-E611-A8A0-008CFA110C64.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F09F04C2-8CF7-E611-9956-02163E019E57.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FE1F7958-CBF7-E611-A87D-02163E019E2C.root',
] )
