import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1F3B6EE4-9ABF-0E4B-BF29-0112AB08EC76.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/450058B0-8E81-334F-8134-51127F48599D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/52ACBB10-D550-BA47-9E36-D56D17E1A4AA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/59F5F2F7-762C-CA47-AB3C-7D0ACC9264CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8E25983D-7E80-084A-A9D9-609E872C21D6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8F209DFD-5B9E-FD4C-9540-48AD7B2BA327.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B41D464E-07BD-7346-A77E-A7A264AAE11F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/BE3E8ECF-7DF9-4241-81D1-5ADEAAB27C52.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CFB28075-4C20-B840-9004-DC5C54D3AB94.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D19F1074-C237-7B4E-B95A-394223B3A949.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D50D24CC-72DF-3D41-BFD7-D88084E9953A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D66D3B14-815D-1647-9ED3-98EFA38A5B5F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E56EF624-EC30-2B4D-A21C-C9236AC4BD70.root',
] )
