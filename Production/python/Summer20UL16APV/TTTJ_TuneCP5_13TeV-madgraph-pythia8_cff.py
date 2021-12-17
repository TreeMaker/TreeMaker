import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2520000/3E887390-C28F-CC40-952F-70FEB4E6CF09.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/0123EBE3-3AC5-BD44-842A-748C047A903A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/696614A1-9063-A248-AEFF-DC34ACF80B65.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2530000/D2BDEB7B-53D1-494C-9A6B-61B98625571B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/3C4DDCC1-DC73-064D-87E0-504381547FDA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/2A71C5BE-883E-474A-89DB-97D0275864E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/7541B358-6B40-1E46-A741-2CC57572C97C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/DE194F2A-546E-2746-AEDD-E784B43027CC.root',
] )
