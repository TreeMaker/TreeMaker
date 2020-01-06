import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3078B344-58EE-E911-9E7D-FA163EC9558D.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4ECFD9EC-6902-EA11-83BA-5065F38142E1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/5445C18B-86ED-E911-96EB-FA163E6C21ED.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1050_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B0369EC3-40EF-E911-8182-FA163EF17F2E.root',
] )
