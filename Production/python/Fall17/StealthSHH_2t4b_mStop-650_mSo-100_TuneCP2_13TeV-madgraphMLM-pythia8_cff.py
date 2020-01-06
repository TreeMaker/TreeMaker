import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/2261C86C-A407-EA11-84B5-AC1F6B0DE2EA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/3654357B-A407-EA11-901B-B49691386CBE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/448095F5-A307-EA11-B843-5065F381C251.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/609473C4-A307-EA11-A781-AC1F6B4D1FAE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/80CC9AD1-A307-EA11-A646-A4BF01287CF8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/A644026C-A407-EA11-9CBF-0CC47A7C351E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/AEF906D8-A307-EA11-92A2-D48564593F96.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B0BC5D75-A407-EA11-821D-3417EBE64BE8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BEE32BC3-A307-EA11-869F-FA163E093A61.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/C4FD2756-AE07-EA11-93BA-B499BAAC0694.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D8506273-A407-EA11-829C-7CD30AB18982.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/DE4A2574-A407-EA11-96D2-AC1F6B596102.root',
] )
