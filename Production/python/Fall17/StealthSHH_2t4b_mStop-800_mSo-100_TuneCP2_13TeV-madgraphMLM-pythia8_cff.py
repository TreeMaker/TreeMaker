import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/625B4062-3BFB-E911-8951-0CC47A544F5A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D26CE2AD-710A-EA11-9B87-AC1F6B23C7DC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D4532CC6-710A-EA11-A55F-0242AC130002.root',
] )
