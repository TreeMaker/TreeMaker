import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/162217BB-1A08-EA11-B113-A0369FF882FA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6475B18F-1908-EA11-BEAC-AC1F6B23C94A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6E1E2A7C-1A08-EA11-ABB6-0CC47AFEFDF8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/72F1036C-1A08-EA11-A05D-EC0D9A822666.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/AEA36076-1A08-EA11-8670-A0369FD0B228.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1150_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/FC487843-1A08-EA11-8903-0CC47A4C8E3C.root',
] )
