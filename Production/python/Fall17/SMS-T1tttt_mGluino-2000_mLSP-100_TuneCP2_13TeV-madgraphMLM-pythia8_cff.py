import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/085DC8C5-EDBB-E811-B3CA-EC0D9A82220E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3E6E77B9-A4BB-E811-9203-A0369FE2C094.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3EB34F14-A5BB-E811-83A5-1418776378DD.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4E0483FD-A4BB-E811-B9F9-0CC47A1DF81C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/648E16AB-E1BB-E811-BA14-0CC47A0AD668.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C2F7367E-A9BB-E811-BAE4-B496910A9A24.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C495BAFA-A4BB-E811-8B13-44A842B2990B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/CEC5B2C3-A4BB-E811-BFF1-0CC47AF9B2F2.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E840F0E6-A4BB-E811-BBBE-0CC47AA992B4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/FCBA6DB8-A4BB-E811-9927-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/8C804A6D-02C7-E811-A86F-A4BF01025C07.root',
] )
