import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/08A98519-11FE-E911-9A4D-24BE05CEFB31.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/18A7D317-11FE-E911-87B5-F02FA768CCC8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/265C153A-72EE-E911-9BFA-FA163ED3B5B0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/70E013F6-10FE-E911-8A7C-246E96D14BC8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/8EFB10CB-F4FF-E911-A7C8-0CC47A7C361E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/96ADBF55-72EE-E911-9BF4-FA163EA2C96F.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/B274ABED-FBFD-E911-BAC2-FA163E14C484.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/BAEA0786-ACEE-E911-8BEC-FA163E39DBA6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/D02472BC-ACEE-E911-AA75-FA163E016D51.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/D4A020FA-ADEF-E911-A4E9-FA163EF0622C.root',
] )
