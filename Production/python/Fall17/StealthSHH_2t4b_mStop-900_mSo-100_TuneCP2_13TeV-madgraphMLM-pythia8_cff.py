import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/4026497F-DBFF-E911-B7D1-B8CA3A708F98.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/56EA12B4-92FC-E911-B456-0CC47A5FC495.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/822CF08A-DBFF-E911-B884-90B11C0BD684.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/909E0AF0-57FC-E911-B0A9-AC1F6B0F6758.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A8412873-06FC-E911-9EB0-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/B2850B51-8EFB-E911-AB66-0CC47AFCC69A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/BCFFFAEC-B0FB-E911-932A-0025904CF976.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-900_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F095E057-03FD-E911-8C70-509A4C83EFAB.root',
] )
