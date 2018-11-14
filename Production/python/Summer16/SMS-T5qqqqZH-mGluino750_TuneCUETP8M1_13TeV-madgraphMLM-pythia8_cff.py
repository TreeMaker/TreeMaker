import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/167DF5E6-6EF7-E611-9F32-0025905B8590.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4A5582D2-A8F7-E611-BE2D-0CC47A4C8F08.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/68427A63-6FF7-E611-AD9B-0CC47A7C340E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/76C43ADF-0CF7-E611-9EC2-002590D9D8B6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/963350DE-13F7-E611-AFD5-0CC47A6C14C8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A203941B-50F9-E611-8BB8-0025905B8590.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A86FBBD1-0CF7-E611-B124-1418773425EA.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/ACC2B676-F1F7-E611-8F13-FA163E2CE8FE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C042C756-0EF7-E611-94D8-008CFA111330.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C09DB181-25F7-E611-B7B5-FA163E0EF12F.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DCF98484-1CF8-E611-A70D-A0000420FE80.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E63AFE68-6FF7-E611-97EF-0CC47A4D75F2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E6AA4801-BDF7-E611-833B-001E67505A2D.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino750_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FA735DA4-28F7-E611-B985-ECF4BBE1CF30.root',
] )
