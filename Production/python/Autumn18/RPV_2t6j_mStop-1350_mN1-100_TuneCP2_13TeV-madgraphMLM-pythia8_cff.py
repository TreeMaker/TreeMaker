import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/130AAAAB-9E4E-FE4C-BC74-19746625CB50.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/255988BE-3C5A-D54E-8E89-88FC6F210F44.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/404BBAE0-63DA-1A4B-BDA0-521016238ADF.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/875F2FF3-24CB-4449-9A56-E1863542EBED.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/9BF92F85-6221-074C-87DE-166A50632EC3.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/ACF5167D-BB48-4642-A70B-829B94428BC1.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1350_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/DF311342-9405-1F4E-A4D1-1076048739BF.root',
] )
