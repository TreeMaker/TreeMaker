import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/0A8CE40A-E1F8-E911-9894-20040FE9C7DC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1075E23A-F6F8-E911-B086-008CFAE4535C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/14B2A0FF-F0F8-E911-B797-90B11CBCFF9C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/405643D7-F6F8-E911-87C6-B8CA3A709028.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/7C8273BE-FEF8-E911-9D9D-44A842CFCA27.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B8FB7572-1107-EA11-B2A1-0CC47A4C8E38.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E2592A6A-E6F8-E911-85C5-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/EC9CFF6A-E6F8-E911-9DC6-0CC47AD98CF4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F09C05F8-E0F8-E911-B55A-0025909082A2.root',
] )
