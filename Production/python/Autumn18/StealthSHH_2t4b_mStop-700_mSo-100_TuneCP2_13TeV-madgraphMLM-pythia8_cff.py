import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1D5AA3E3-4499-F94A-B4CF-C2D1FA1AE316.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/436BA4E0-C9DD-6147-8DA7-B500B4658CA1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/50DBABC2-5C71-C844-9B6C-B10F6F9B8E43.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/74F9F5FB-807E-2F46-A4AB-BB2F5E7E8B9F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7B2EF3C2-75A4-BF4D-B8AF-E9DFDFF715EC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8C3CEC8F-E9C7-5C4A-A45F-69A9E5700DD9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8CF2AE04-FB6B-494B-AB68-E5AFAF9B37DB.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/920202B9-F46A-7049-B474-97DACFAA19C8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9B5C975D-EC67-A946-8A54-92E3AD8738C5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9CA46803-5345-B845-8DD0-9A81D4FAE47F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B20BC527-893D-FD42-B54E-962EE3D7B6C4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/BECFC1C7-921B-7645-A420-7D115137A3B7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CACB3F3A-2178-F241-9DC4-844ECBEB06C4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CE684334-9F4F-4F49-9442-8C06AD91867F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D15E1AF1-BC35-954D-AC95-75A18C3556A5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F04CAE51-B616-5941-A0AA-BEBECD00A93B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F9A2D3D7-0BD5-AB45-94DD-FF6F491C44C0.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/FCDC9A31-08F3-264A-9F65-86AC395A2833.root',
] )
