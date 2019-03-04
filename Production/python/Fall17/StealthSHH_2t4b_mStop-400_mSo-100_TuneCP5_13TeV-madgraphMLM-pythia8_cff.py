import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/0A6F3CC8-8FA8-E811-9AC5-FA163E2746ED.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/0AC6C09C-A8A8-E811-A690-02163E015422.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/14A18859-02A9-E811-8F2F-FA163EA76A4F.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/14DEFAF7-CDA8-E811-A829-FA163E2D6F6C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/3A4A30B1-E8A8-E811-AFC1-FA163E8AF4C4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/461553BC-D4A8-E811-BE76-FA163EFDEAA0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/46DA9899-BAA8-E811-A7A6-FA163E5CAB1B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/4C15E953-DAA6-E811-A59E-FA163EE11B00.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/52F460CD-C0A8-E811-8136-FA163E4F980C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/5EC65FD4-F0A8-E811-A3F0-FA163E5E44F4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/80A03B9B-84A8-E811-B356-FA163E3135EA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/AE23DFB7-B3A8-E811-929D-FA163E716EF8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/BE2358C0-03A9-E811-856A-B8CA3A70A520.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/C20D3F9D-ACA8-E811-BCD6-FA163E57B0C7.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/E89B3816-EAA8-E811-8936-FA163EE25D43.root',
] )
