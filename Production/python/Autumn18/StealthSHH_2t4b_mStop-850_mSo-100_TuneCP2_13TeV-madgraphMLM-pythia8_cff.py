import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/08C6D259-17BA-D942-8D6C-F84EF98EAEBF.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/274B3B7E-A779-0F4B-9105-914B23046D7E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/29CDC169-0DD4-994D-89F5-7E39687C076B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/5953D28C-4368-D544-8CF3-EB75D69F17B7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/5F7F39A3-0220-EC4D-82C4-C810644ABA5D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/7B3AF1F6-57D4-E348-8877-7FFCA57A3CC5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/88500A40-1BA2-7242-BE78-BD63F2179F4C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/A1EF0FAD-B63E-1B43-8675-26FDC612E0F2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/A7F83472-2857-6646-95B3-6DD60CC55BD4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/B2A356E5-9536-E14C-B216-E6E71C388DCC.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/60000/DDD3668D-2039-B048-817D-DBCEA463CF50.root',
] )
