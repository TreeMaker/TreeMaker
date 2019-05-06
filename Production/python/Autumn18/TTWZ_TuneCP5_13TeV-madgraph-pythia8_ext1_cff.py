import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/314FD8F6-A8B0-FB43-8F71-C35317D61C91.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/4D3386C6-8583-E04E-B57E-675F5C617655.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/57D14EBE-76B0-B749-A8AF-3DB0D991F89E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/89E943EF-D40E-954F-913B-E0E66B35B2F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/9FC747F3-8F17-AB4C-A54F-2815435F9C01.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/BEFA2678-5A75-504D-9A7F-68454D77290D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/CA307A95-9E93-DA48-8B56-0D5962C1DD5A.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/D2A2EF1B-F932-8F43-B65E-F64CEC06B077.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/1D52EFBA-E1EA-364D-8AAE-99D83EBEE868.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWZ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/3F4D82DC-E3C4-5546-80D2-B592049BFC3B.root',
] )
