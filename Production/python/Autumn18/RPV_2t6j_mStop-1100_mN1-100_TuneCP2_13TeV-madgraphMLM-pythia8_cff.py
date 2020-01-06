import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/30756478-6F0A-6943-9258-D2EAD080E6E7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/37637B30-BF1D-A745-ABD3-2029F59511BD.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/724D82AD-9A29-6248-A91E-7FA9601C2BF9.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/75DE788A-D193-5F4E-B690-B16376536082.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/98A9FA08-E88F-7347-B19E-13B9C0743094.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/DBA10FC0-A592-9B4E-88C4-E274A919D57B.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/240000/F78AC2AB-4F61-0D4C-AD6F-47E1EDB76B3C.root',
] )
