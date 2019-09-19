import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/2BAAA2BB-6D8C-0D46-8C3C-EDCE57AE666F.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/7CFA4B9D-6E77-2843-8E45-21C1ACF3C828.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/8D4BB693-2FAE-EA4E-8588-776A14EBCF80.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/8DC72BEB-EFE5-D940-9E5F-21A05E1BC0B0.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/A394366F-5C6E-DF43-AE84-F4EC1936F0AB.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/A6362742-F52C-9A4C-81D3-2D40D4E662DA.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/BAA7075A-777B-0A4D-9EB4-FE025592CFE4.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/CBE481C4-B24D-B44C-8535-C3B5BF34C37B.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/E89B752A-5734-2A46-9CD0-241040C25007.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/EB533F13-5548-914E-AE88-D7C3320CD9F7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/260000/FEF1E0D2-15BA-1944-999B-C503BC4ED53D.root',
] )
