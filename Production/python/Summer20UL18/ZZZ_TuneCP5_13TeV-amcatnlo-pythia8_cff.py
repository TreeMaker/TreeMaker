import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/02A23304-1761-744C-9FDF-3367BA249387.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/1CBEC4FE-E95D-E14D-96C9-7F28903EAB38.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/2FDD5D5B-36ED-534B-AAAA-B29523AABBBB.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/34EEBC6E-3FCF-E449-82B0-FD7409FCB3F9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/433917B9-3054-E84A-914E-40B912087BB0.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/4CBA940A-2943-954D-9B7F-F3C66148B415.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/53E0A8E2-806C-7B46-B6D0-4EEE691B8919.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/56802686-6B5F-5649-BE51-14FDAA3E443B.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/62F43006-E83F-0E46-B979-74D253C7CCDD.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/63A6A71D-C444-4340-8AAA-7CE7787D632D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/7AC65565-6569-C24E-80FE-2E13DA92AFC1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/7B94A922-DEF7-0C4E-865F-53538C5F976D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/8C56084C-C908-5247-A4A8-E6214005E18F.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/A1A24847-ECB4-AE41-A8BF-D518582CEDE1.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/BCF9DF5C-0A75-6E45-8753-9E3C65522C33.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/C644879F-3E5B-2443-9F65-979739CED8C4.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/CEB6E039-B5C4-DA41-83B0-0CF35B76C5D9.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/D552D9F3-C1A6-ED41-8F77-19CB495D5888.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/EA2C75CD-1C6E-8541-B6AF-53389F298CEE.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/EED66DB4-3051-3D46-8545-2B3752123AE7.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/F68810CD-A438-934D-AC8C-AA2BC3BED4A5.root',
       '/store/mc/RunIISummer20UL18MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/230000/FCCA34C2-6898-2643-8FF4-BAF922AF8660.root',
] )
