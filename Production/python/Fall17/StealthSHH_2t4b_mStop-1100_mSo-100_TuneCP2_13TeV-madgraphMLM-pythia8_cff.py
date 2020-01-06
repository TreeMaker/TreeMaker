import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/06469F24-62F7-E911-91F9-BC305B390A59.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/50A78868-61F7-E911-AC87-B8CA3A709028.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/862DA43D-64F7-E911-AAEB-002590908F8E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B0D94550-61F7-E911-A324-F02FA768CB3C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1100_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E6CCC274-DDF6-E911-9F86-B4E10FA31F63.root',
] )
