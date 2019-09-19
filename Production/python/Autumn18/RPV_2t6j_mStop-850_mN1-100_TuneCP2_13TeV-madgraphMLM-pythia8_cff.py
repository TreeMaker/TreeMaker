import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/1425AAE2-B8FF-4D4B-B7F5-D826AAD50469.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/2459F859-F89E-6C42-ABD0-F44BE8D4F4D6.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/8F227676-ACEB-D04F-A6B0-9C30518F3074.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/A4CCAB63-3198-3C49-99B3-EE1D1E7E1137.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/B40721EB-1CEF-9141-90D1-4ADEE1374C93.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/B7E9612D-E70A-C14C-A0E9-97499AD55E65.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/BEE08D3D-C348-4D4B-B9E8-D457890F3DAE.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/EF2B04B5-911A-6D49-840E-D43490495060.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/FEE7042F-E0AE-7549-9850-F8067D8C1B8E.root',
] )
