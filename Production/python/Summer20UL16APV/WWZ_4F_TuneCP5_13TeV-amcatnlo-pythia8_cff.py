import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/16337DA6-3ECB-E44C-A021-9FFB27A762B3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/1B6069B8-5AB5-1747-A142-0E31BF365DA9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/3011EAA1-6995-DB49-8CB4-4D85C5D9D1BB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/36E3F90E-7F18-3449-88B2-4824A7D7E567.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/527E9D00-EE1A-C541-82A8-453F042CBA9E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/5749A224-F01C-A144-94E9-87ABB1675D00.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/698D4800-C2E3-DA44-BD7D-4803B7EFB38A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/94C24963-6B67-044C-89C5-1D802266BF57.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/AAD7FA8D-A905-344D-A421-4AFF2CA20539.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/AC9C4AB1-788F-A443-BF1B-6A3932CFD4A7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/ADD4ADBE-6F91-0A43-9E31-57C0AFA3A317.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/C42C2543-B912-B242-A9FA-68907A8F5452.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/C5CCB1FD-DBB4-F546-9891-A05E799F0853.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/CD3ECD98-7D49-984B-898D-90210582CDEC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/D1A5B62D-80A9-1149-A3D3-20AB9BDAF25F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/DB02BE6F-A0DA-3440-AF8C-FE9EA9759F8E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/DE45D768-7326-5F44-8A93-28BABFCE2101.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/230000/FD3A709B-1101-B24E-A8FF-EC0F7E8289F7.root',
] )
