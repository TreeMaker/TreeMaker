import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/3A91ACF2-E806-EA11-A1F4-0CC47AB65044.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/4A2607C2-F205-EA11-A66E-AC1F6B23C9D8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8C64FCB2-4808-EA11-8C31-0CC47AFCC6C6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B052D660-02FB-E911-A7B1-AC1F6B23C970.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/EE3F723A-CCF9-E911-A597-AC1F6B23C9FE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FC304623-2305-EA11-8E46-D4AE528EB025.root',
] )
