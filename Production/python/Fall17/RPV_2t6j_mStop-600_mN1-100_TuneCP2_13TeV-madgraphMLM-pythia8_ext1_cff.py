import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/502DCADA-AFC9-E911-99C1-B496912ED604.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/A29FB0F4-AEC9-E911-A101-E0071B7A45D0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/CCEDACDF-FDCA-E911-8303-0CC47AFB7D8C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/E89DD5B7-63CA-E911-9A91-FA163EDE6D4B.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/FA461626-AFC9-E911-B65D-549F35AD8B95.root',
] )
