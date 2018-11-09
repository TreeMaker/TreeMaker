import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/04F872F2-C2F7-E611-8171-0CC47A7C3408.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/20EADA64-68F6-E611-A814-0025905B85FC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/50B6ECEB-C2F7-E611-A3EE-0CC47A4D7666.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/5467D376-ACFB-E611-93DC-02163E00B0DD.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/6CFF6921-73F8-E611-988E-001CC4A65D70.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/7C773C71-87F8-E611-B6FD-0CC47A4C8E14.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/987DF914-ACFB-E611-AA53-FA163EAED918.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/A6CD4611-A4F7-E611-8664-0025904C66A4.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/B23E3ADA-A6F7-E611-B4C7-002590AB3A82.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/B84F6B8D-87F8-E611-9330-0025905B8574.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F03A446A-00F7-E611-9B75-047D7B2E81BC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F6D751C5-A3F7-E611-A962-00145EDD783D.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/48CE8A4B-47F7-E611-8FD7-0CC47A78A30E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/6E025798-7BF5-E611-9896-0025905B85EE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/760CA0A6-4DF6-E611-97A0-0025905B85A2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/AE2747A9-18F7-E611-9735-5065F37DD491.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/C8EB024F-47F7-E611-A19F-0CC47A4D76D6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/F2C02763-6BF5-E611-AC63-0CC47A4D7644.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FA189AA8-4DF6-E611-B0CB-0025905B855E.root',
] )
