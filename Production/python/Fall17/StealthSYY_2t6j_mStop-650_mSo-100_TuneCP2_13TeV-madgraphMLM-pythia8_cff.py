import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/44439439-7116-EA11-B39E-0CC47A706D70.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/9E0DFA97-2416-EA11-8FEB-AC1F6BC67D50.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/1A72042C-0813-EA11-ADF9-AC1F6BAC815A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/24A21C59-D912-EA11-A7B6-0CC47AFCC65E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/3A73453F-D912-EA11-829D-A0369F7FC934.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/52FBDA47-EB12-EA11-996B-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/5CAE2840-D912-EA11-AF68-0026B9277A25.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/7C96B037-D912-EA11-B32C-AC1F6B0F3A26.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/88077C3A-D912-EA11-91C6-549F351EB336.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/88840F66-D912-EA11-B6FD-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/9209BC34-D912-EA11-B5D0-6CC2173C3DD0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/D01B3421-D912-EA11-A9BC-24BE05C618F1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/D6044C74-D912-EA11-AE9B-00266CFF0A88.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/E8E22947-D912-EA11-8630-34E6D7BDDEE8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/EA309437-D912-EA11-9C94-3417EBE6FFFD.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-650_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/FC1E7C9F-D912-EA11-AA78-0CC47AD24D28.root',
] )
