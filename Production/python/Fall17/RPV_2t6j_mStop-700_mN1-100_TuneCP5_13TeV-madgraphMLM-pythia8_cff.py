import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3620734F-559D-E811-8FA5-1866DA87D4B6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3EE9564A-559D-E811-B91A-B49691091B34.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4618754A-559D-E811-98B0-001E67E71CC7.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/70C1377D-559D-E811-9B0F-E0071B7A5540.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/766CE9AB-559D-E811-B320-F01FAFD9CB34.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E0958874-559D-E811-8351-001E675A6725.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E4B8A841-559D-E811-B6B1-0025904C66E8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/FAC709D4-559D-E811-8AE3-008CFAC94240.root',
] )
