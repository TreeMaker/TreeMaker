import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/2C5DA068-7700-EA11-A563-484D7E8DF078.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/34ADA22F-F8FE-E911-B8E2-CCC5E5F2B52E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/4CCE583A-4300-EA11-A034-002590D60056.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/84F89982-7000-EA11-9ED4-0090FAA57C10.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BE64C64F-4E00-EA11-8112-00259073E50C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/EE8B4B3F-84FE-E911-ABCE-002590907882.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F468D7FE-A0FE-E911-9DF5-24BE05CECBD1.root',
] )
