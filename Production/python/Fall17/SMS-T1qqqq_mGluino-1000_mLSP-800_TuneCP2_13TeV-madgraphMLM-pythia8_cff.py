import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2C74AF91-A1BF-E811-AC18-44A84225C911.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/36CD43D9-FDBF-E811-B194-AC1F6B0DE2E8.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3C2D5976-A9BF-E811-B267-24BE05C60641.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/ACBF5DB3-AABB-E811-A1F6-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B685079A-AFBF-E811-863E-0CC47A1DF818.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B6917A8D-A1BF-E811-87FB-00266CF82EC8.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/BAA7F028-0CC0-E811-B596-509A4C748AC4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/FA4347EA-C7BF-E811-B056-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/FC9784F5-BABF-E811-9B28-0025904C51DA.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/FED56146-ACBF-E811-92D2-0CC47AFC3C9C.root',
] )
