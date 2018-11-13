import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/AC4D1BAB-1DC4-E811-9E33-3417EBE2ED22.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/08D3DED0-A6AC-E811-A2C0-003048CB8584.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/0E7C5B91-A6AC-E811-BD9E-0025905A60A8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/1002F21C-A7AC-E811-B39F-B499BAAC0680.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/201D80C8-A6AC-E811-A4ED-A4BF0100DD3E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/48CDBE0B-A7AC-E811-BF71-6CC2173D46A0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/5C52B888-A6AC-E811-AA22-FA163E257F51.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/9E3F94B5-D8AB-E811-AA28-24BE05C44B91.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/D2B45AC2-A6AC-E811-84E7-008CFA197418.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/F0E2C29F-A6AC-E811-94B8-7CD30AD0A32A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/F2D4EDC1-A6AC-E811-8897-44A8421274BD.root',
] )
