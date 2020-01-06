import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1CCE3F96-5A08-EA11-B298-AC1F6BC67D4C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/26D4A416-4708-EA11-AE65-0090FAA58224.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/34895A72-8B08-EA11-A800-0025905AA9F0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/40A3CA02-5B08-EA11-8CE1-008CFAC91100.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6C7F3F77-8C08-EA11-9E27-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/C05BA66C-8C08-EA11-B857-90B11C1DBFB4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E0E5DE2E-7E08-EA11-9159-0CC47AC17502.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E2EA4085-8C08-EA11-9083-90B11C0BD63A.root',
] )
