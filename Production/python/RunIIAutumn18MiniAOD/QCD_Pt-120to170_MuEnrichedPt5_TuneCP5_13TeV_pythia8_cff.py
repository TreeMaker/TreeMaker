import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/FlatPU28to62NZS_102X_upgrade2018_realistic_v15-v1/270000/9441F6C7-007D-CE4F-BE04-E9B412179352.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/FlatPU28to62NZS_102X_upgrade2018_realistic_v15-v1/270000/9FE66927-2432-4C4E-9C29-798E287434BE.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/FlatPU28to62NZS_102X_upgrade2018_realistic_v15-v1/270000/F02CAE0E-03DB-DC4D-AC31-62358BF2D748.root',
] )
