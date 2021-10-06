import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/2B559840-175B-4A46-AE9B-67C6A7CF7381.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/4DB2C82F-FFBD-CF47-82B6-E44E9713E2BF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/4FDABE90-920E-6A4A-B06F-467D5BD59008.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/6E7899C6-F45E-F546-8083-13BA66983DD0.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/7591F459-B301-0641-8744-FE3ED2576661.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/77238C89-6979-2A4B-9F62-6BEEF71F1B7E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/772C6417-F44E-514E-9F30-BBCE5BBB0606.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/8BC1BDFF-A846-AD45-B0D9-CFF24A4FF30C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/91549DA8-A565-B648-ADB7-30B93C39C1D1.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/926DAF4B-35DB-A34E-A955-C19709FEA125.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/BA44AF92-D3D9-694E-A587-E20CAD0B6B52.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/BE373944-02F2-3342-8F59-12BE469527EE.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/DC7A10E5-6A35-084A-846B-5DBFEC95CE63.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/E3F01BCC-01C4-5B4C-BB1D-6373BFF6F1B4.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/130000/F9CBDD5D-6492-FE49-9720-6181324FC52E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v3/1310000/9FADA4C5-13DF-9A4C-B282-92952F2ED72F.root',
] )
