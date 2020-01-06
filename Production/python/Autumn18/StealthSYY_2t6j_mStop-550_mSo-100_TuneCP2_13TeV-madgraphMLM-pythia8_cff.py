import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/19AAC252-896D-A846-922E-4523798C5679.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/20955689-D54E-ED4D-A30B-2656A583D4AE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/24A1AE29-01EF-B442-B6A5-1A68F6A7689A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/4E4D186D-23D8-2142-8F3E-F027A4765235.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/51362D7B-ED45-6243-AAF3-29BE3B260187.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/62D1BB29-C2F8-644C-A8C6-F78678962FC9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/70455029-D8BB-F743-997A-4FF47793FB41.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/813ACB24-E321-2F46-9AA1-AF12D23B7B30.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/861A942A-AD52-9740-BF0D-D9088E041603.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/9474E739-D3AB-174E-B6EF-4A5CA1EC7D48.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/96C1DDD8-E8CB-C747-9E13-8A8809E29DA5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/98EB9D2E-1016-CD46-8A5B-30AD9E67DF2E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/B50E7814-E8FB-0047-9B76-4C40F56CE221.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/BA4BA6AF-9005-4949-83A1-7CA5E0584B5F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/BA90343C-D91C-D442-8B41-74F46A3D0D58.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/BF15D876-7EA5-4F4A-BE42-1482AD16CE41.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/E2B6847A-04D5-ED4C-92A0-B5FF9C044D89.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/ED01D865-4E09-764C-98E0-2E80AFA7924D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/F02F1C4C-FC7B-2A46-81CF-677998BEE17F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/F8CBA973-5425-4A4E-8D25-F07766ABE2E5.root',
] )
