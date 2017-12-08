import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/080B466A-CBF6-E611-8741-A0369FD8FDB0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/12411E76-4CF7-E611-A961-20CF305616E8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1E2DBA77-4DF7-E611-A829-1CC1DE192582.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/261BEA02-4CF7-E611-96DB-B499BAAC039C.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3A2CCF6F-4DF7-E611-A8BC-D8D385AE870A.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4EF6F6E9-28F6-E611-AB12-009C02AAB484.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/504481CC-C0F6-E611-AC0D-00145EDD7389.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/506F6BD9-4DF7-E611-B1AF-0025905C4264.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/58C04808-34F7-E611-935A-047D7B881DB8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6EF55E69-86F6-E611-9F87-C4346BC08440.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/748A4997-22F7-E611-8E3A-02163E015DAF.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7C761234-50F7-E611-9E87-00266CFFCAA4.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8C018D74-31F7-E611-BAE6-0025904C7F72.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/90864873-4DF7-E611-845A-B083FECFC6ED.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9C47730B-0EF7-E611-9A95-001E67792650.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9CB6447B-72F6-E611-9C6A-C4346BC08440.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A42342AB-4CF7-E611-AB56-0CC47A7C3610.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AC83BE3B-F6F6-E611-9CB9-3417EBE47FCA.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D23237AB-4CF7-E611-980C-002590E7D7DE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D2DFDF1E-4CF7-E611-86E8-FA163EC94B30.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E42478AD-0AF7-E611-B99C-FA163E23659B.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FC17E18F-0EF7-E611-84DF-7845C4FC35EA.root',
] )
