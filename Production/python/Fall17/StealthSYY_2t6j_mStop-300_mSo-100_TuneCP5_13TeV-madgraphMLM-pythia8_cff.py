import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/16968395-7BAC-E811-88B2-24BE05C616C1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1EA44ACD-ADA6-E811-8A4D-001F29082E74.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/202FC22D-63A0-E811-8585-B8CA3A709648.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/24F12F0B-A5AC-E811-A6A0-0CC47A78A340.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/3061C73E-9AAC-E811-AB90-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/3EA0D30F-DFA6-E811-9C5E-D4AE52900EF9.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/5CE54ADC-CAAF-E811-9B1D-00266CFFC7E0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/5E01372D-8CAC-E811-87C2-FA163E498136.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/5E9876C3-DEAB-E811-9D7C-509A4C7288FE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/662FB6D0-C8A3-E811-ABAE-E0071B73C630.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/70F69244-F9A6-E811-9430-E0071B7901F1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/72D9C418-90AC-E811-AD9F-002590490020.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/7828FEEF-06AD-E811-BCD1-00259029E670.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/7AE83108-72AC-E811-A49F-008CFA197CA0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/8A73455D-6BA5-E811-ABAE-484D7E8DF05E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/8E03458D-DA9F-E811-9710-008CFA1661B4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/B6584F23-B39F-E811-B68A-F01FAFD691F4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/BC025D16-DA9F-E811-8189-0CC47AA99436.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/C2BCA343-B7AC-E811-ACA5-484D7E8DF085.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/D283D8C7-F2A4-E811-A120-001CC47D7BE0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/E23348BD-C9A3-E811-80C5-1866DA7F94F2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/EC7D9AF8-E7A3-E811-B294-6C3BE5B5F210.root',
] )
