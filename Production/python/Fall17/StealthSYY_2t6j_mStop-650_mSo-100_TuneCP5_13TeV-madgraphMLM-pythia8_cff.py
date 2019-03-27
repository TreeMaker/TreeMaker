import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/0E788554-8CAB-E811-8056-001E673987D2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/0EA5C8C6-8BAB-E811-B64C-246E96D14C5C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/208C0C93-8CAB-E811-8E0D-0025905D1D00.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/72FEA490-8CAB-E811-BD3B-A0369FD0B364.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/86A6A416-8CAB-E811-8FBA-842B2B6F550D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/CE291206-8CAB-E811-BA96-0CC47A0AD6C4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/D6C4E006-84AA-E811-80E6-001E67E6F7BA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F6B24404-8CAB-E811-8BEB-5065F3819232.root',
] )
