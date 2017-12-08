import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/323A9A33-E0F7-E611-8FAD-0CC47A7E6980.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3CF02479-40F8-E611-B21C-02163E013982.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3E55D3EA-E6F7-E611-88E1-FA163E6BF37A.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/3E7252CD-13F7-E611-BB23-0CC47A7E0134.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/4CD2D99C-17F7-E611-9396-3417EBE64519.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/5837733A-41F8-E611-819D-001E67504F55.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6A27C141-3FF8-E611-9BFF-A0369F836372.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6EC0984F-2BF8-E611-A857-C4346BC7EE18.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/70D57D8D-32F8-E611-85D1-00266CFEFE08.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/84F6E740-EAF7-E611-81A9-44A842CFD5F2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C8E8DE49-40F8-E611-9A98-FA163ED2118E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CC93BBD7-D6F7-E611-A2EE-002590A371C4.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/D89D2A8F-3FF8-E611-A518-002590A831B4.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E2E015C0-3FF8-E611-8B37-3417EBE64CDB.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F422A3DD-28F7-E611-B7AC-848F69FD4568.root',
] )
