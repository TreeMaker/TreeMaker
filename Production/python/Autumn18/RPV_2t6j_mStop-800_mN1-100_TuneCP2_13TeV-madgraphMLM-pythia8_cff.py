import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/16FA87E9-6B87-3F41-ACBE-EF48389DF899.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/5C13BE3F-8F97-C14B-92CF-B9502C847CC7.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/6E938B82-6383-8940-A1D9-2FF2F31185B9.root',
       '/store/mc/RunIIAutumn18MiniAOD/RPV_2t6j_mStop-800_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/270000/8779FCF1-7C2A-3E40-A926-B453BBE8C115.root',
] )
