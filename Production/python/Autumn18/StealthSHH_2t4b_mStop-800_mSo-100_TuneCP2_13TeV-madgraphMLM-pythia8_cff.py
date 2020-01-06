import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/1077D5B5-35AA-2B42-9D66-B4F4D4F4CE9F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/2CC4E0F6-2E42-D140-905C-D1E12DD1186D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/4D785D9D-AAB1-7346-A613-245DC66588CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/5AAB68F6-71AC-EE44-8402-5E68BC79A13B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/6DA93E37-980F-8146-9E30-E23B12C88F38.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/82D6D050-4079-C942-BA7C-8EBB4BB41895.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/98D8A0AA-FED4-9A49-98D0-982F7ABFD67B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/9F7E57D4-D324-9F45-BE0D-03DC6FBC5597.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/A69B8E11-BB87-2545-9B2A-81F6E14F3290.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/D8C1BA6B-B75B-FC45-9255-29ED45BA9F0E.root',
] )
