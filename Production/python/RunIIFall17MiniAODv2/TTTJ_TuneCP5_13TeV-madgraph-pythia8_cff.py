import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/40000/724A579A-82A8-E811-9E1F-001A649D475D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/40000/728D81B2-89A8-E811-BAC5-001A649D4DE1.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/40000/98A89FB2-89A8-E811-974C-001A649D502D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/40000/ACD869DF-8AA8-E811-AB37-001A649D49C9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTTJ_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/40000/F226F2B9-89A8-E811-8697-001A649D492D.root',
] )
