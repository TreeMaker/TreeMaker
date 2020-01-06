import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1228141E-4EFA-E911-A677-AC1F6B0DE33E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1AD4BF1A-9BFB-E911-B7CD-20040FE8E8B8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/56E5954B-33FB-E911-8F7F-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6446CA03-9BFB-E911-8AE8-0CC47A2B04CC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/78C9B9D9-43FB-E911-B863-008CFAE450AC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/A4467D5A-92FB-E911-84BF-0CC47AD24CF8.root',
] )
