import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/7376A282-712A-FB4D-B553-F715F66C5067.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/CB06BC4E-5C9C-1D40-854E-F3026196C967.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/499DC5DF-6834-EE4F-8DF1-F9CCF08A8DC9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/68EDA2D7-44E5-1F4F-9484-D3193CC908BF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/84B44B9F-FD08-3343-872A-70CDF5AAAD07.root',
] )
