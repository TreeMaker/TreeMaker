import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F8727133-5E00-EA11-B73A-44A8420CB0CE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/1AEBEA7C-65FB-E911-92E6-0CC47A7FC73A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/20B6C5DF-88FB-E911-9BA4-0CC47A5FBDC1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/341141D8-E0FC-E911-89A7-20040FE9CF4C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/48AD2138-6BFF-E911-81AD-A4BF010114DB.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/904F5C2A-F2F7-E911-9CB6-90B11CBCFF8F.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/9AA51C53-03FD-E911-B922-008CFAF5052A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/B6108872-6BFB-E911-8D1D-0026B9277A4C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E09EC3F2-65FB-E911-A613-AC1F6B0DE33A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/FA58984B-5FFB-E911-8A7C-FA163E660C3A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/FC64B5D3-56FB-E911-B143-0CC47AB65044.root',
] )
