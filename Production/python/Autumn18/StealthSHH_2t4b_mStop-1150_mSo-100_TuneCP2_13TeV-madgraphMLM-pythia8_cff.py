import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/0A252E9F-7DBB-5140-8550-74A335B58CBA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/1D9141DC-EFC1-0A40-BE3C-C7173ABF6776.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/25D127DD-5196-D849-8C73-BBA4682F9288.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/3FD58FBB-7C4A-A24B-9795-79201EB51958.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/52442AA1-0134-4B41-B84C-56DF2D183E3B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/5A98686A-DA22-A940-A38A-E51BBF53DBD2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/A831D780-9ECA-C14B-BA4B-B5300E4A09CC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/E38B508F-08DD-704A-9C39-C6B6BEE3D818.root',
] )
