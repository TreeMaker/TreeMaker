import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5C460C23-E342-E811-8847-A4BF011256A8.root',
       '/store/mc/RunIIFall17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/6E327865-F042-E811-8822-A4BF0112DF14.root',
       '/store/mc/RunIIFall17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/AE859FE4-F341-E811-A293-A4BF0112BE12.root',
       '/store/mc/RunIIFall17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B6C8F1FC-8D42-E811-9734-1866DA89044E.root',
       '/store/mc/RunIIFall17MiniAODv2/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C4D6693C-1542-E811-9B5A-1866DA87967B.root',
] )
