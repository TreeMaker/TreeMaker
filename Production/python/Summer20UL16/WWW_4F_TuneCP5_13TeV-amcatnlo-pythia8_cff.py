import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/5DA583F0-136A-9849-A663-39D03F305B16.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/AF96A63E-7F91-B749-9864-CCE5FAF0133D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/C9B8F310-0CC1-5A43-90E2-8FB4B66644E2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/7E9F6365-8200-6B42-909A-BB44DF002CD1.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/A487D9F8-E29A-634D-B962-BE088258D8EE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/AB831BFF-7598-3B46-8401-0221206E3486.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/E0063277-67F2-9341-8DA2-5BA728064844.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/1617ADFB-3D8B-4F4B-B251-E5AB3752D111.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/169C4768-F599-6748-A9F2-4CA11FA674AA.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/4083477B-FE98-B54A-9FCE-A88F4CAB5D8D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/9E402043-372B-C840-B1B2-C9A08651CA6B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/C1B4E0BA-17F6-C648-AE10-11284D296677.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/317D4878-CED7-114C-89DC-EC0B41B4EC30.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/586FA99D-2911-AF4B-B50F-C10A59D130C5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/85DFE88B-AD37-CB4A-9139-2424F014D246.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/1000232B-BF34-C84F-A1FA-5D3717C40519.root',
] )
