import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/48A8569A-B108-EA11-98A7-C45444922AFC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/4CC49FDD-AA08-EA11-92EB-24BE05C4D8C1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/7A86D869-C709-EA11-8B28-0025904B5FD0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/88134A0A-C108-EA11-A579-6C2B5990D1BF.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/96B73C26-6DF6-E911-BDA8-AC1F6B23C77A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/9AF8E259-C808-EA11-8FAD-AC1F6B1AF18A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/C0F20398-B50A-EA11-8CE7-001E677924CE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/CE7A0B49-70F7-E911-BD40-0CC47A545096.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/DE445B77-A50A-EA11-887D-1CB72C1B6C32.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F082B907-CD08-EA11-ADE5-1CB72C0A3A61.root',
] )
