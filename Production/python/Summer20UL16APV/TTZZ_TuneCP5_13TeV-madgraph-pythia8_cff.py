import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/0EF5FC68-5E7D-924E-A7B2-7D37FAD07D4D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/12BE1A7D-9553-1245-BD8F-D10B82CBACB1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/3F65ADE5-56F0-8E4D-B754-B10829DBA32D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/4DC8B22D-C977-4944-A120-6311A7193F54.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/521DFAC1-0461-6B44-B674-27EB3916ACED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/56CD2F9F-A6BD-7F4D-B462-CDF4084F0264.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/63C11F64-A5D4-EB4F-9EBD-1A61478B34F1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/674592C5-B44A-8945-A522-247B1AED7E45.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/81B2760F-1575-7245-8543-F30A7820B845.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/8CAB6681-F990-8044-A42D-071202B22134.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/92DE4895-DA84-9E41-93C9-553D498F3187.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/9A51CA64-4F41-7E42-97B7-CDB6F68E6586.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/B260346E-BC16-2942-8C42-2A7E8F6016C3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/BC2BAC22-CB33-FE49-86ED-2F741D8E1A76.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/C8CC9C2B-F4A6-E64D-BC2E-7964CF3304A5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/DEF890E5-1730-9C47-95A0-A12EE66B5A29.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/E636CF44-BC55-EE43-BCD0-3F023A70AEC4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/E6B7F576-D7D8-0E41-81C8-D4293F0AE2F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/E911DE5A-5281-1444-AA70-26FC9CC19819.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/EB69D49C-E8CB-1347-B6D8-69E9F347726A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/TTZZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/140000/EFB4BF52-927C-C24D-A2C2-FFC59FFC3A2C.root',
] )
