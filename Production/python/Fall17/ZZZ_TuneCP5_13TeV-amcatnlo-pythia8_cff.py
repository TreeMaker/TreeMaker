import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/5EAD99CB-5743-E811-B513-0025905C42F4.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/A4CCB4FC-9143-E811-8EBD-008CFA1983BC.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B818C7A7-8D43-E811-A4CD-008CFA14F9D4.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/DCE1F444-9943-E811-9100-008CFA197B44.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0246996E-A642-E811-A9DB-0025905C54F6.root',
       '/store/mc/RunIIFall17MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/10661591-8E42-E811-91ED-0025905C94D0.root',
] )
