import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/12230311-04DF-154F-A09C-E6073E32A25C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/2E87E727-77AE-EC4E-BE4B-2A153B33D470.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/4D70980B-07BD-C945-A25D-103EC9BEA051.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/571FCD19-D8C5-FB49-972E-8813F8591F24.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/71BB8E08-A279-644A-9B54-74804144546E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/82DDAD5C-F473-5143-8A33-3AF537FB8F4F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/90707CCB-861B-8F43-B4BE-E98EA45B137B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/D5CF58C7-4705-3A4D-9428-E94491C76A47.root',
] )
