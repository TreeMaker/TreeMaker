import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/05FD99B8-0449-A144-AF9A-726C7DA6E74C.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/08796D9B-E01D-D744-A557-9F47790820A4.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/094BA012-759C-1B4C-89D7-DC7137EBDA96.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/0A2B7790-5FBF-9745-A3CA-176A4FB92125.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/12EDA4ED-CA04-6A4F-B024-DB513C10B61F.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/26B42E54-4F36-A447-8CED-B92A27E4946B.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/5A2C047F-2630-1E46-A078-5941F9C707F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/78F84A65-8B20-A642-A842-1FE7A098ED82.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/88450E84-06A0-9041-95F1-D5409236A91F.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/89BEB208-3A34-1647-89EB-14F96A69ECA8.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/9D4C7A3B-574C-D948-B515-64FB84D4E631.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/A40AC3A7-3415-C243-9FA2-CDE5CBD0BF85.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/B26A07A3-81AD-B647-B4A6-295B409A6C1D.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1250_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/EEFE5219-E188-7745-8CDE-D167DA9298EE.root',
] )
