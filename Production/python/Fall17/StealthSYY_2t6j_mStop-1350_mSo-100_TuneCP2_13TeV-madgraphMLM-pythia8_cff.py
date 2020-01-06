import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/00A7E061-E9FF-E911-92A0-B026283422D0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/18832194-8DFE-E911-BBF4-44A842CFD5E5.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/244568C8-7AFF-E911-9F26-246E96D14C5C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/88898BF8-7EFF-E911-BF30-0CC47A4D9A50.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BA3AA7C3-50FF-E911-87CF-0CC47AFF24CE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/C275AAE5-06FF-E911-837D-90E2BAD5729C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D80953F1-B2FE-E911-B807-EC0D9A0B3320.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1350_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E28DD04A-2D06-EA11-A68D-AC1F6BAC7D1A.root',
] )
