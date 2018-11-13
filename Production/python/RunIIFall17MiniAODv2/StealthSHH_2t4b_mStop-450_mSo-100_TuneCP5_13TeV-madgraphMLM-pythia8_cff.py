import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/106BB0A7-95AC-E811-8040-0025905B85BC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/12EE0F22-96AC-E811-BA9B-0026B9278637.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/18A01EBE-57A6-E811-A02A-001E67E6F878.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/22764CA3-95AC-E811-A561-0CC47AFB7DA8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/2A80759A-95AC-E811-B87B-AC1F6B0DE454.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/40A2D003-23A5-E811-8509-003048CF3C22.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/5AA46697-27A6-E811-90A5-002590A3C96C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/627F397D-7CA6-E811-97D6-A4BF0112BC14.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/8C27096B-4CA6-E811-8B9E-A4BF01159534.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/8CAEC6B6-02A6-E811-A0FF-A4BF0108B2F2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/90D59423-96AC-E811-8BEC-B083FED04276.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/92C663B7-95AC-E811-A133-A4BF01125DDE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/BA0C7CD6-95AC-E811-8451-5065F381E1A1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/BA185EDE-95AC-E811-B505-90B11C443C9E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/C4D07C25-96AC-E811-9D89-0CC47A1DF800.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/E25FFA9B-06A5-E811-82F4-A4BF0112DFA0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/EC059F23-96AC-E811-BA4B-001E67580704.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F2A29904-3CA6-E811-AE0C-A4BF011255D0.root',
] )
