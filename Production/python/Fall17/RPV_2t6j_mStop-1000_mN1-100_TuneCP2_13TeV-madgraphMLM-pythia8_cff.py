import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/029914B8-94EF-E911-849C-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1807952F-EBEF-E911-A539-246E96D10990.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/22FCFE19-5CEF-E911-99B6-FA163E4A8187.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/621587F2-50F0-E911-8A2E-002590DBE1B2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/96F2C3E6-AAEF-E911-9AC7-0025905A48C0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D8419312-6AEF-E911-BAAF-7CD30AD0A684.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1000_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/FA0A6956-A9F1-E911-9700-C45444922AFC.root',
] )
