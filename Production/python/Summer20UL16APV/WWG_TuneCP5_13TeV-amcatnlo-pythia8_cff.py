import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/0786A174-78A0-3D4E-8C2D-B1C94A722102.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/124AA5C8-71D7-E94F-A683-4BFED0F14EED.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/1F9E9F16-85A8-9748-AB03-610B4EF64F5F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/3B117D1B-E619-7E46-9458-B5A5F61643F4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/72C1297E-5751-C34A-B3CD-ADE4CF05F8F0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/7BA3A5C5-7FD1-8B4E-BE47-8DD3EE99C3CF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/8A97C1F9-D3A7-9242-B60B-7AD26F728B36.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/9BB9FCC2-D8A0-5742-BB59-1A25DCEE2CA2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/BA462D05-8F44-9147-90E0-B1C244A2EFEE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D3407661-6FAA-5E4C-B14B-2A9B70E04482.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/D7B04EF2-3CC7-FD4A-B6E7-9AAEDA205CBC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F1590949-C931-534D-8CC7-7E94F3436BAC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F4C90B2A-F6DA-6344-B735-03CFA12C9E06.root',
] )
