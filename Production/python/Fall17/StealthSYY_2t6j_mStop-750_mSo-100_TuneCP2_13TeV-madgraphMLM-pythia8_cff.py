import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B025CAA1-26F7-E911-9CAF-FA163EC939FD.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/50E41ADE-EBF5-E911-9BFF-0CC47A5FA211.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/5C18AA6D-ECF5-E911-A0D7-FA163E57250F.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/7A00E692-26F5-E911-BB92-002590494C82.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/DE5FF747-ECF5-E911-8774-509A4C9EF8FF.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E4375CD8-EBF5-E911-9359-3417EBE7446B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/EE6C2253-EEF5-E911-A4BF-34E6D7BEAF0E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/F2D3F6F5-EFF3-E911-8FD1-40F2E9C6AC5E.root',
] )
