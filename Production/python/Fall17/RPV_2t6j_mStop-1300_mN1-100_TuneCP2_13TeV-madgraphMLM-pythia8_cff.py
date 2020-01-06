import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/50BF0AD5-12F9-E911-9BFD-FA163EFB9E63.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/60CD49F8-2DF9-E911-8AFC-0CC47A7E6B00.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/98AA48E2-16F9-E911-908E-7CD30ABD295A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-1300_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A86AE5AF-3FFA-E911-B23B-38EAA78D89AC.root',
] )
