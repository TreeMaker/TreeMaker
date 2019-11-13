import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/38EB0BD1-6F82-A44F-BF83-86E69D8B150E.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/3A2A6249-6A8F-D24F-A36F-4C441E9A6DF1.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/4041B441-D1EF-534F-B6BB-C2C07AB51940.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/795C52C1-CEAD-7F44-9D3B-8737D8AC54DE.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/BF2BF1E5-ECC7-9042-A2A8-B906E018E1F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/30000/FBE70B20-508A-984A-9CBF-95601BA7E965.root',
] )
