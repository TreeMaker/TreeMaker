import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/12E245B7-A6F7-E611-A92E-008CFA000B68.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/20F6FD88-D8F6-E611-9FD2-F04DA274BB9C.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2807EFC5-A4F7-E611-AB66-002590DE6E86.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/38032394-0100-E711-8E2D-001E67E6F89B.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/3C9F2E5F-F9F5-E611-A146-A0369F6369D2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/48F9306A-ABFD-E611-A8B2-02163E01A35C.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/506AE655-CFFB-E611-8325-FA163E4334BE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/5637F7D0-A6F7-E611-AFDA-0CC47A57D164.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/58BF1B36-D9FC-E611-A352-02163E0143E9.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/621AC8CB-24FB-E611-8530-6CC2173BC370.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/661817BF-D5FB-E611-8B7E-FA163E023ED2.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/66220C22-A5FC-E611-A1B8-002590495244.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/68CC18BA-DCFB-E611-81B3-02163E00AFFC.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/68CD0B5D-A3F8-E611-8440-D8D385AF8AEE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/7E3C39ED-0AF9-E611-AD97-002590DB920C.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/9AC1FBCE-A3F7-E611-A15D-0023AEEEB799.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/A4745AAD-C8F6-E611-8044-D8D385AE8BAE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C2619311-71F6-E611-B7CD-0025905C54B8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/C85D9161-C1F6-E611-9085-6CC2173D6B10.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/EC88E81B-73F8-E611-97F1-44A842CFD5BE.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F2374204-B4FC-E611-86DC-02163E00CA1E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/F83F704D-C8F9-E611-82C9-C4346BBCB6A8.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/067FA4C8-C8F7-E611-AB91-0090FAA57910.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/64155C61-66F7-E611-B38A-0CC47A7DFF2E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/9C30D2A7-E8F6-E611-BC99-001E67E71BE1.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/A6DB2ECB-3FF7-E611-B976-001E674DA1AD.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/CEDE0880-7BF7-E611-9113-0CC47A78A408.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/E600B860-01F8-E611-830C-6CC2173BBA40.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/130000/FAF1B6C9-B2F7-E611-B480-0025902008CC.root',
] )
