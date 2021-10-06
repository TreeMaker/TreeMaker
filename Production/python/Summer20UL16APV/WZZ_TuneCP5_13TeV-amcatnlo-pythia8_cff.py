import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/25ABF385-02A1-104A-8D34-9D31C7E05EFE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/A41BCEE4-CD64-FC4D-867F-F3775F98F196.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F7A77D2F-0172-AB49-B895-307DAF5DBC52.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/12D68FED-5FE1-8146-8ADE-94D08CE3B098.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/173B195B-4C80-3444-A20E-6EB0EDF38382.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/AA54A8CC-64F6-0D4C-BCF3-57E936AC9CCF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/BE8E6581-6D3D-594F-8BF9-B4D29B0398ED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/8942ABDA-EDBC-9649-87FC-9B6C7AE1437A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/015D657E-9A75-7D4D-8DF6-B2FF03855F87.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/345F3BF3-7E11-824A-B875-243E2765A603.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D13470BC-F3F2-A344-A17D-99D31B9B5E67.root',
] )
