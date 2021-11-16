import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/3AFA9BDF-626E-D540-A049-E6C26DB57746.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/1C2C723F-EEF4-FF44-9C2B-567ABADE9DC4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/6912161D-15F8-504F-9362-8EDC0B05E679.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/7178F7FA-6A7D-D648-884A-484041308413.root',
] )
