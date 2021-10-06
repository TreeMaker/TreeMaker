import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/4B3266F8-0BBD-8E4F-9C22-C1CD4215484B.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/110000/B7938D13-51DA-0A49-9F60-24B35CD8B506.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/230000/ED10DA2B-65C8-E34F-A625-56EF195B4468.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/15DCCF8D-EAA4-5440-ADA4-9C74CC03B926.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/36B95868-69C7-5B48-A299-4AD74ED88BC6.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/240000/42B249C7-149C-FF4B-9529-6BE6DAD0AC23.root',
       '/store/mc/RunIISummer20UL17MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/30000/98A69386-E4DB-8449-AC6C-632B81090AAE.root',
] )
