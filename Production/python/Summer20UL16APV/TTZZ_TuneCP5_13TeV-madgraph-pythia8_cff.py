import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/1CD79EEA-DD6A-004C-A0F9-CE5F092ECE54.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/8F3756C2-FB12-9F4B-8B34-8C767C23A1B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/FEC6AC91-C121-CE43-900A-2A3F10C15CE3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/097B863F-6A41-544F-8556-59668DE24A8D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/4682FA3D-C9ED-D341-9754-CA50A8B7ABB6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/E32D0B27-8DF7-C445-9256-300193FE2FF5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/EF9E542D-1DD9-7C4A-B5FA-8467B2BEDE3B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/5917C32A-4ADC-D142-92A1-18C29D18B4A4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/6C46CD84-F9CD-DB43-9450-FD1596598CB6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/7F9F0EC0-9A27-9D46-82FE-F29346988C2E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/9766DE6B-FF97-4044-8211-5EF527526856.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/A68923CD-EF7F-4E4D-B122-C1C2D1A63279.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/B098DAA6-392A-3F44-80C7-04FA67A2551B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/D24E4D58-3813-0549-A007-E6F92CAB0EDD.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/ED783D0A-D272-2A46-B8D0-92FA5405529E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C4200E76-4929-9C4A-96FC-5086D5FA3EE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C7A30754-7BFF-394C-BC72-39EFD6A195E6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/D431DEC5-661E-D64F-BF78-DC7D18C54117.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E2CA3DEA-AE75-BD42-BCB0-22CB05649F8F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E33EE462-1147-494B-8564-0E0CA71F0355.root',
] )
