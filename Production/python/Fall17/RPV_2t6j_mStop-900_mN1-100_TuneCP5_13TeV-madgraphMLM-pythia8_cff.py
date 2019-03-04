import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-900_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8C206EE8-509E-E811-B0DF-FA163E8D6D0D.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-900_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C8783DEE-059E-E811-AAFB-FA163E408EE5.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-900_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F0B6F843-E49D-E811-A25C-0025907793F4.root',
] )
