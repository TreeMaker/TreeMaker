import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/048BB260-C742-E811-98EB-0025904C4F52.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/344004DE-5843-E811-9188-002590E7DFFC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/BE36158C-0F43-E811-802D-A0369FD0B3B0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/CCBD8827-A842-E811-B724-0025905D1C54.root',
       '/store/mc/RunIIFall17MiniAODv2/TTZH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/D6845F08-8442-E811-81E0-0CC47AF9B51A.root',
] )
