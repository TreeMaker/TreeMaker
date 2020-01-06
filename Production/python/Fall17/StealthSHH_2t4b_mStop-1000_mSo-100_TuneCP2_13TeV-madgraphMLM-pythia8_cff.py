import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/40D57F44-DFF6-E911-84A0-AC1F6B23C846.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/601C9265-C1F7-E911-87FB-AC1F6B23C970.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/240000/EA34B751-80F8-E911-8090-E0071B7A8560.root',
] )
