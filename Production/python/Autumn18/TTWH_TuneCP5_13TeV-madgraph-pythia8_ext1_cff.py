import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/1BBC8585-2959-8846-A2F4-8EC7155F53D3.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/2B56E88F-051E-394E-8622-7F0B080EECBE.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/53644FE5-972C-AC45-9420-D6216C96DE50.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/56005D93-6C7B-E042-8E0E-7F7EA2C6E0EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/6DF215CF-2C4C-B14B-A840-4470CFBB93B4.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/7117A8BB-B7C5-6C4B-A29B-270AEB209D70.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/76B5CB88-D21B-2B42-A40A-4F93B995BF68.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/C28EEFA5-0353-1343-A015-B5010CE510DC.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/C92CFA9C-E066-C746-A66E-DD30BBBF1705.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/D49855BC-6C60-2C4C-8463-7571F6FBC297.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/D9E9C6A3-6034-0E43-B531-113867377CEB.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/20000/F288B4A7-2E3F-E043-8F11-F9ADC72CF984.root',
       '/store/mc/RunIIAutumn18MiniAOD/TTWH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15_ext1-v2/90000/3FB26CE2-EC79-1144-9E7A-3874F1CE0A2B.root',
] )
