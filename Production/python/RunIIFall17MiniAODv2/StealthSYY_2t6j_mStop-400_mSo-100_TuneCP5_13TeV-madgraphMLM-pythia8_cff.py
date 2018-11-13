import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/08D8B29A-D29C-E811-B6A1-FA163ECF8DB3.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0E02EF93-839A-E811-8F9F-0CC47A7C35F4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/122759AF-D29C-E811-8DA6-008CFAC91B60.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1E02050C-7399-E811-8F66-A0369F310374.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/20AA7E4F-839A-E811-A4B9-001E67DFF519.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/40FCA5B9-D29C-E811-9180-1866DA890658.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/449948A0-9C99-E811-949A-008CFA19743C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4AB066A5-099C-E811-8FC5-E0071B740D80.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4E8B7ABB-D29C-E811-AFB8-A4BF0102A4F5.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4ED0D0B4-4699-E811-999C-0CC47AD98F78.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/68A3EC11-D39C-E811-A29A-0242AC130003.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/703E338B-4D9C-E811-93B8-0025905B85A0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7E51E5AA-D29C-E811-AB1C-A0369F836372.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7E999DB9-D29C-E811-9569-0CC47AA53D60.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8E2516F5-D29C-E811-BD2A-90B11C444042.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/BCB321A0-C69A-E811-92F9-008CFA197E84.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D2AB71A2-D29C-E811-8F7D-EC0D9A8221E6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E28906CA-D29C-E811-967F-0CC47AA992B0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/EEF2CC56-2B9A-E811-8D8F-0CC47A7C35B2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F06B174B-BB9B-E811-A789-0CC47A4D76D6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F0CDAFA1-069B-E811-992F-0CC47A4D75F4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F2F857FB-1A99-E811-9D3C-1866DAEA8218.root',
] )
