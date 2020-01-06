import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/0E9252C3-E608-EA11-ACDB-0CC47A4C8EC6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1E9C4662-7009-EA11-BCD5-801844DEF100.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/44303D4E-8408-EA11-9E6D-008CFAE452C4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/92D25A59-0609-EA11-A694-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/A2119A59-3708-EA11-A235-AC1F6BABF8D5.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/F615B809-7F08-EA11-97A0-0CC47A0AD6E0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1000_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/6C062448-E40A-EA11-9610-6CC2173D8740.root',
] )
