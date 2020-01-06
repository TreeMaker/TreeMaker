import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/0E7A9603-D5F4-E911-AA87-BC305B390A66.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/463A920A-D5F4-E911-9494-98039B3B004A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/5EED5070-D6F4-E911-9085-B8CA3A70A520.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/90A5C701-D5F4-E911-A8A3-002590DE6C48.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/D80BE985-D6F4-E911-9DD6-FA163E5FF39F.root',
] )
