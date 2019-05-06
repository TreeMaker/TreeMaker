import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/03B92DAA-ADB6-0A48-8FE7-D93B786DEA24.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/B2C65A09-03ED-7A43-9EB0-9DF6144E7C40.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/54B6528E-93B9-E44F-A11F-984677243CD3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/5693BC13-8AE9-4A4D-A681-8D06B151C2EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/5B502EE4-6F49-6E48-BCF9-87D2680C60AA.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/909BD8C2-961F-FB40-928F-7DAA978F901E.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/98E8AC00-D8D5-F143-876F-B2237B0C58D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/BE94C7AA-741F-D84B-92FD-80598A2F310D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/C93B83D5-4757-C74C-A5BC-567AF346D061.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/D5D6D8B7-8174-D44D-836B-4675D60980AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/DECE0240-D536-754F-BFF5-DFBFDDA8782D.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/F514651A-19C9-0947-8C42-3D3E659B79C2.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/270000/F7CA1458-6B44-BD4F-96F7-202959D4DEB1.root',
] )
