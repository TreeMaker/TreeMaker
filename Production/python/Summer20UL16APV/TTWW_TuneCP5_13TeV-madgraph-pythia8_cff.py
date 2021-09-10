import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C1377B64-542C-D741-A372-80ADF3CF6E8E.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/CEF243BF-0D9E-F548-8A16-99C87EDAF9CC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E8580FB7-43D4-1740-8C79-801A2047B210.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/0619352B-7C49-6642-BC10-1E0B20FB07D9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/32C9B981-A9DF-694D-82FD-415DF5C16C3F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3E08C46F-BC6C-424C-8390-F69DE6F2BB41.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3F8C2C18-C514-0C42-A079-7C15D63B7A93.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/587D3689-4AC9-1949-972C-75F77159F82C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/83A4EEEE-62D8-6140-83E5-1185B20A9EAF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/12075357-D6E5-D44A-B652-0BD9F2DB6CEB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/120D57D7-F563-0E47-90A2-69F8030F28AC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/715A50B1-5C76-2F4D-BDB1-94A071458657.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/DD4D3EA5-A924-584C-BBC7-9E509197D5A3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/D2EFE1D3-5242-4342-BAF1-57906ECE4242.root',
] )
