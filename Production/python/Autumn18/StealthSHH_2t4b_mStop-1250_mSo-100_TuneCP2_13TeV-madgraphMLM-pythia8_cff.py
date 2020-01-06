import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0C51F999-9FAD-3D46-BD02-D9486CAD9E47.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1101CA25-4452-D149-87FF-9AE8F7C24D9B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/13B93C32-D289-F048-9B07-0DBC86806522.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/15DBB949-6A89-9144-88CC-59CEF6CE6886.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/26286A47-718C-8344-A5B8-27D71CB87D38.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/3379F3DF-6915-394E-9FA8-6E0454F58FB6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/436E6B32-527C-B144-B52A-E999814FEBAF.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/6FCEC329-4A2F-D24A-85B6-6CC9685EBF28.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/85F28869-C929-A74C-808E-6949DF4988EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8A6DDD0F-1399-5241-8B83-30E0C62F259F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AB9C77F2-1166-CA43-866D-0D3020323E0F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CF3175CB-5031-0741-9C94-558AD5C40C3E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D27EFA6C-321C-8448-B870-08DBDCD46643.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/42433F6F-4B01-2648-9DED-C8F0CA11D637.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/94574477-6B36-1E42-937A-CD4DD9FE8B6A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/95A55ADF-C808-D54E-B449-27050ED25446.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/A36E63C1-3FCF-8F4A-A988-08B56D4300B8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/A97B9282-A190-724C-8FB0-3F6226A617BC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/E46837F9-6F5B-E94D-A577-3272CE878A3D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/FDF653EF-C421-514A-98A6-24F6F9060983.root',
] )
