import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/145C077D-EE4C-CF46-BC1F-05F442711A4B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/1AB212C5-1954-D24D-A527-C366280DE2D2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/55E47541-0621-8946-8267-2EC2C9F88845.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/D5DBC0A1-F9E1-F74F-AE4E-29893D0B6205.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/46AAA7FB-69D4-484E-B4BE-BB8FBC5E326E.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/482F8B3B-00EF-774F-BDC3-249A00F99BE9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/6E2041BF-3E11-0047-B555-81DC196FD53D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/E97E8BF5-B473-F248-BC72-131E27BD6AA0.root',
] )
