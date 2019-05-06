import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/404E59ED-90CF-F449-8345-D4970143FAE0.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/41614CD3-9B39-3D46-BE65-7BE6B85BB75C.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/417B4361-1402-C24D-9088-4D7C595B012A.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/43B2F7C4-9B12-C242-BD15-EC9CF84B99BC.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/497E9353-9D95-9541-809E-13D0540344DD.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/68D34B74-3968-9341-A00F-CEDF24F2A7F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/986CFDC9-924C-AA46-94DA-8107A526FB1F.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/A17FAF1F-3190-584E-ACEA-AFA1F0B207CE.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/ACB4F978-EF72-714D-A24A-EA99FAE220F9.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/B12A945E-7C68-5740-8EFB-3CCD736329E9.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/BAE90A1F-7A73-AB48-80BB-18E065183E22.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/DFCAF81B-964D-6F47-AA2B-5136CAB6F4B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/E0989373-CA8B-8B40-BDC6-18B02A9308A7.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/100000/EB477D77-854E-0247-9074-EE837A21E254.root',
       '/store/mc/RunIIAutumn18MiniAOD/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/80000/3D3B3D54-FA5E-6F45-8D43-E2D1B0DDAB93.root',
] )
