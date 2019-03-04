import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1ADA8CB5-27C1-E811-8FF6-7CD30ABD278A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/60118559-27C1-E811-96EF-24BE05CE1E31.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/60E0C387-27C1-E811-BADE-0CC47A6C1058.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/A8CE847C-27C1-E811-976E-008CFAC93E88.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-850_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B6C5E00F-2EC1-E811-9662-002590FCF738.root',
] )
