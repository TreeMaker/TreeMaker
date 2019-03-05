import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/0424FE17-DC5A-E811-8CDE-008CFA198258.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/0C1E08BD-BC5F-E811-8BEF-A0369FC5D5A4.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/24651DFE-CD61-E811-9C3A-008CFA1979A4.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/44EDA22B-886A-E811-B4A6-008CFA0A55E8.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/461861D3-285F-E811-8974-008CFA5807F0.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/8206DCF9-CD61-E811-B94B-B496910A026C.root',
       '/store/mc/RunIIFall17MiniAODv2/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/BC4D6AA1-B95F-E811-BA2D-008CFA1979A4.root',
] )
