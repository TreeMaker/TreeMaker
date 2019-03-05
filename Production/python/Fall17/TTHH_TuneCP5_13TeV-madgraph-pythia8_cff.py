import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/08E63C69-8042-E811-B3DD-FA163E277950.root',
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/12189C3D-6142-E811-910A-0CC47A7C357A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1A7D3D47-C741-E811-AB26-02163E019F3B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/24FF89C6-CE41-E811-B25B-A4BF01125B58.root',
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/78F431D5-CE41-E811-8DA3-00259021A39E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9AAC7C67-5441-E811-A7E1-0025905AA9CC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FC18B7CA-CE41-E811-AF73-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FCAB94C8-CE41-E811-9B18-C4346BC80410.root',
       '/store/mc/RunIIFall17MiniAODv2/TTHH_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FE2C92C5-CE41-E811-A385-0025904C66F2.root',
] )
