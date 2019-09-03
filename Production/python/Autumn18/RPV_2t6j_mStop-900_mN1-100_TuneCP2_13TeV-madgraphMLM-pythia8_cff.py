import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/0791FAB4-5731-C545-837D-9BD4703405A4.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/247C7F1B-0549-D04D-A5B4-009BA02B8070.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/76D4D66B-54A7-6142-8D97-89F8716D9232.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/8335D070-F198-9C40-8775-36A698947613.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/953DE91C-9713-1B42-910A-B173007E46B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/AE447F09-0710-7940-B907-5D98297867E0.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/DBD98305-1FB5-8E47-82D8-FBCEBA6EBED4.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-900_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/130000/F30BFBAF-3464-0D40-B18F-87A4A4624C44.root',
] )
