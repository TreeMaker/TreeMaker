import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/04E0EAA4-409D-E811-A82A-0CC47A4C8E66.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/746C64A2-409D-E811-8B9C-00266CFF0AF4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/82CE5FAA-409D-E811-938A-E0071B7A4550.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/90B1515E-409D-E811-B855-001E677926B4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/941EB782-409D-E811-B038-1866DA890B94.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-800_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B4A88780-409D-E811-81BA-1CB72C1B6CCA.root',
] )
