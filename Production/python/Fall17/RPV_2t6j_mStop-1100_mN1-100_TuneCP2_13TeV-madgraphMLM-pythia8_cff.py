import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/3A9EF849-A61B-EA11-9481-AC1F6B0F39FE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/0EF9D975-F503-EA11-A063-AC1F6B56768A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/2E271F59-E303-EA11-8FC6-484D7E8DF06B.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/62E65B2E-8304-EA11-94C5-0CC47A7EED28.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/74638A6B-E303-EA11-82FE-A0369F7FC54C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/A046987B-E303-EA11-8E96-AC1F6B1AF18A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1100_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B245B17D-2504-EA11-9F8E-FA163E3B081F.root',
] )
