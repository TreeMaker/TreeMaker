import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/AE007E4F-F7FA-E911-AD11-FA163E009BB9.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/FEA00BBE-1EFB-E911-8505-FA163ED4BE3A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/00CC4E79-E6F8-E911-9992-38EAA78D8ACC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/0CDB0E7F-50F4-E911-B581-00215AA64960.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/1E85264D-E6F8-E911-A9B7-7CD30ACE23EC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/30F0A1D0-C4F3-E911-A195-F4E9D4DF0F50.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/3240AF25-DEF3-E911-9F2F-E4115BCE00BE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/386CB7F8-2FF4-E911-95C1-98039B3B0036.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/44BF1589-E7F8-E911-BF79-D4AE527D07CC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/4652076B-DEF3-E911-8E37-C4544423E434.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/4A9CC22F-4DF3-E911-AD6E-FA163E92D43A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/4CE6E36D-E7F8-E911-9684-008CFAF52264.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/50B40F4C-E8F8-E911-AA69-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/52CE39A2-E7F8-E911-A288-AC1F6B0F75D4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/6A95A721-F3F8-E911-AA23-0CC47AD98CF6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/8E6EAD26-18F9-E911-A80B-002590907802.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/901C1157-E8F8-E911-9C15-34E6D7BDDEE8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/90255834-57F3-E911-BFC3-FA163E613B91.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/9C972C9A-6CF3-E911-8C09-FA163E20DB46.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/AC7C4A75-E7F8-E911-892E-1CB72C1B649A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/AE2CB6FD-4EF5-E911-8937-3417EBE706C6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/B0DC745E-38F4-E911-9198-FA163E6BC02C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/B2AB4D1E-A2F3-E911-8D1C-00E081B705DA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/BE17F55A-90F9-E911-A93F-AC1F6BC67D4E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C23416A3-1AF9-E911-B5EA-008CFA197B1C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/CA013634-EFF8-E911-B056-44A84224053C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/CA382BDA-AEF3-E911-BAF7-A4BF01287D34.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/CE13EA6E-D1F3-E911-929B-D4AE527D09D6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F2592E1C-2BF3-E911-AA9D-FA163E93A54D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F65B09C0-D7F3-E911-B5B1-F4E9D4DF0F50.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/FAB14758-CEF4-E911-BE95-AC162DA6E2F8.root',
] )
