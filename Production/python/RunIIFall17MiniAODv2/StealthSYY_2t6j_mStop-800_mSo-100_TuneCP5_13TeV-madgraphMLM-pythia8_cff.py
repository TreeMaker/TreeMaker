import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/086D1227-6598-E811-AEB1-24BE05CEEDE1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/AA52D324-6598-E811-825D-0CC47AD98BC6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/AC3063EC-6498-E811-A90B-FA163EA0A52A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E801E228-6598-E811-8300-68B5996BD98E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/FC762D31-6598-E811-A0CA-1866DAEB1FCC.root',
] )
