import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/D0AD9E98-440B-EA11-A16E-00259090775A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/00E11E5B-5B08-EA11-90E6-C454449229AF.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/22C9D79A-3909-EA11-9FA9-002590E3A286.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/2AA62CEB-5508-EA11-B0F4-484D7E8DF0FA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/2E68B591-B008-EA11-9A74-0CC47A4C8E16.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/30B8067E-5808-EA11-98C4-A0369FE2C020.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/3EFB1C66-6308-EA11-BB65-AC1F6B4D50CC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/46532ED0-6908-EA11-B2CD-20040FE94280.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5AB35F8F-AF08-EA11-AE86-1866DA7F9435.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5C93ACC6-6208-EA11-9960-008CFA197B10.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/F20B294C-DC0F-EA11-828A-F01FAFE37F1F.root',
] )
