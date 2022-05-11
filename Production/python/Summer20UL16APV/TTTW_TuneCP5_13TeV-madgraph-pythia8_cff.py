import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/567F37A3-10B1-D347-BFED-59E2FEE758DA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/F8653D1D-BE7D-BF4A-A03F-4062CB06E1FF.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/A0555470-4175-C94A-92CC-EB1E17BF5EC2.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTW_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/F8C78EE0-B387-4A42-8474-09191998FD0C.root',
] )
