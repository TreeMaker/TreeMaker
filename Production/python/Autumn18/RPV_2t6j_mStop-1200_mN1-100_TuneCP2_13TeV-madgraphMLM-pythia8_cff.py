import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1200_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/01BD4242-B8DF-B943-B8FD-27A22F8CDADF.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1200_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/1EAA3D7C-A9A3-274F-8A2E-732314E3F2E3.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1200_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/2539216D-C2C0-EC42-820E-E55F0D487155.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1200_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/5C68C003-4177-2241-BB15-64AD9FFAE0A9.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1200_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/AC3CA7D9-A617-4041-BFE2-A931A5214140.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1200_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/B40E3F45-86BF-1A49-9023-F422CFDBBC24.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1200_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/C4D1F1C2-BB15-4145-8B0A-FAB193136AF3.root',
] )
