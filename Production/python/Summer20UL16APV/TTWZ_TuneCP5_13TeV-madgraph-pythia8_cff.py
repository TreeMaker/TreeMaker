import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/AD222467-9FF4-5E48-BECE-C32C579CAEC0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/350146FD-795E-4042-BD1A-82FF85AFBC8C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4358AFE9-AB37-FD49-B46A-D492FA2A31CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/4DA9E95E-26D2-9B40-9E60-1BB9B9613BF5.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E83DF6AE-C005-8C4F-9D86-1ED0CFDC039A.root',
] )
