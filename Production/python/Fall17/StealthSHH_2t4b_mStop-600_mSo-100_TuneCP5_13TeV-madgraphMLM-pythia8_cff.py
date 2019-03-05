import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/16B9EAAF-CB99-E811-9862-A4BF01158C98.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1EC79DC5-C999-E811-B068-002481DE4818.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/321BB735-CE99-E811-895D-0CC47A01035C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3AD81A5C-CA99-E811-B48B-D067E5F914D3.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/527CE724-CE99-E811-9B28-AC1F6B8DD244.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/62385494-CB99-E811-A0F9-001E67E69E05.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/92800FCF-CB99-E811-BF98-00238BCE463C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D0A9B10C-CB99-E811-9632-B8CA3A708F98.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/ECDF23D4-CB99-E811-92A4-7CD30AC03712.root',
] )
