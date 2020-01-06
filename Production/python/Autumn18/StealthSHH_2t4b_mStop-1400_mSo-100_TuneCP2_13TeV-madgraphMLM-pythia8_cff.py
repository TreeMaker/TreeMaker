import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/19AC6642-F8BA-2047-9BCD-32B009377A19.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5F52FA68-7DC7-1C43-AD1F-B0CA311FEB94.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7228395F-14AC-104E-905B-F1C907866C1A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/96FFE5AE-5445-D54C-B853-D246AF91A9D1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/97FBDB94-D25B-AA41-AD72-18383606D071.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A757407E-9BF6-324F-B0E1-523FA1BC8E80.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AF282BA0-1B51-704C-B737-EF87817EB17B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B49BA7A6-05E6-FF42-93D9-BCF42D2DCA7E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C9858D6D-C5E7-4F41-9A68-E42A076982E7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/CA97D9FD-A287-504D-AAF6-B8271A7A0254.root',
] )
