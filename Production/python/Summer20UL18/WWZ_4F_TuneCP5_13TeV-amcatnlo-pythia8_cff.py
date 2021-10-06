import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/1A3D22C7-368E-D643-8A8E-9C5E4F4E22A3.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/9E07F00D-7585-FE4D-A934-243DDFAB5CBF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/C6D5FA56-5F26-2943-8BE3-DFF2B6DE57EF.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/110000/DD210C19-7A88-B64F-9CD6-69D3B7D792E6.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/230000/6BC6E86A-22BC-3143-B20D-43F33071FD29.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/8A78A4E7-6411-574C-8C4E-E1B87D667F58.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/DBABF39F-9349-DF45-8F2D-7124EAA28E6E.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/C6F01CCE-094B-AC48-B68C-7A12DC0EB27D.root',
       '/store/mc/RunIISummer20UL18MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/E16490A0-5C3B-794E-909E-ABBA3A429817.root',
] )
