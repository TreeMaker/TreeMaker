import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/0E3D3E12-B878-3249-8651-7EC87E1603CA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/118DA8B5-A9C1-BE43-B27A-B3D5DBFB71C4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/119458D7-9885-7648-97D4-7851DB42C39D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/384A650C-4F30-804B-AB65-19B00E0401D6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/4FE1700C-4CA1-0240-9954-4DCACE77D9E7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/6A9D2FB7-6B94-4E47-9843-D9D727EC2B9A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/73C4DC58-3943-AF42-B2A2-2972DAC11741.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/850BD5DF-3B1D-D443-8192-83EA6509DED4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/8A447FE2-B114-EE4A-B973-DBA6CC180AD3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/9635E1C0-9F7F-C04C-BF92-D244E67AF3C9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/20000/A854346C-EB1C-1145-A6C4-1CE6319E0154.root',
] )
