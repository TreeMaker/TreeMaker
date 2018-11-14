import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/04CDB2FD-39F7-E611-B3F3-FA163E6EC443.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/22FE6F81-0FF6-E611-9C2E-A4BADB1E6F7A.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/30681DB3-F3F6-E611-B526-00259029E84C.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3E286C7E-11F6-E611-A2FE-5065F381B271.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4C8782FF-C5F6-E611-8BA1-90B11CBCFF4E.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4E386B0F-16F6-E611-B132-0CC47AD98C86.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/56A07CF2-DDF6-E611-BD6C-0CC47AD98BF0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6A172731-FBF6-E611-B2C8-00266CFEFF04.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7AE68A05-C6F6-E611-89CE-00259021A262.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/808E661D-16F6-E611-A84C-00259029ED1A.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/80E2F85E-11F6-E611-B955-0025905A608A.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/80F7F35F-0FF6-E611-96CC-7CD30ABD2EEA.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8C794086-C2F6-E611-A56E-6C3BE5B5C0B0.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8E06868D-40F7-E611-AB7A-0CC47A78A496.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A6624B90-40F7-E611-B655-0025905B856C.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AADD338E-C2F6-E611-A8C4-D8D385AF8902.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B2E88FA8-4EF5-E611-80D6-0CC47A74525A.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B895B581-14F6-E611-8D58-001E674FCA99.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C414F171-1CF6-E611-9BAB-7845C4FC3A28.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C44FA968-3BF7-E611-9468-02163E01A540.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C8F1EE6A-EFF5-E611-8617-008CFA197480.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CA590F63-1CF6-E611-9815-0CC47A4D76C6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D22F6CEF-22F6-E611-AA97-02163E01A2A4.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F001B4FA-C5F6-E611-A821-0CC47A1E0DA6.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F4F940C4-54F7-E611-8C2C-24BE05CEDCD1.root',
       '/store/mc/RunIISummer16MiniAODv2/SMS-T5qqqqZH-mGluino2100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F8C0AC45-38F7-E611-B145-0025905C3D6A.root',
] )
