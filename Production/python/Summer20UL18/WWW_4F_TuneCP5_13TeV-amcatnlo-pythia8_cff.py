import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/2C979045-A391-214E-905F-3A8DC53BE648.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/AF8104BE-DF6F-134C-A080-BD69F307A89F.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/F95DE254-BE9B-9E41-BDC3-C7C564D02F60.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C30E90B7-0C72-FE4A-B2ED-C90221B5C9D2.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/C82000C9-D34D-6E4E-8428-3DD50456CD8C.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/121F6F5A-09CB-564A-8090-166ED161C24A.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/E1CD139A-83BB-DD46-88A6-AF1E3053BBD8.root',
] )
