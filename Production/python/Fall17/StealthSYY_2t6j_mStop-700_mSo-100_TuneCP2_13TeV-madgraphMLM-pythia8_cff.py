import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/0CC1798D-D203-EA11-B37F-44A842CFD5FF.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/24DAA1B0-3803-EA11-BF7D-509A4C781343.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/28D42256-E202-EA11-9E76-E0071B695B81.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/58E46B6C-3803-EA11-A20D-509A4C9F8A64.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/940F9392-0B03-EA11-A16A-1866DA87AB31.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/9E9C3516-5D03-EA11-B6E4-FA163EE604C3.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/9EB7DBF3-0304-EA11-AC85-0CC47AFF2C3A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B4AF5C28-0404-EA11-9F0F-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/CCC232C3-32EE-E911-AE6A-FA163EF3463E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/DC1ED615-0C03-EA11-A9B9-4CD98F816E6D.root',
] )
