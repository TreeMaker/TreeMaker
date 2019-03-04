import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/0A643428-9E9D-E811-8BFD-0025904C516C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/1CFF3E2A-9E9D-E811-A20F-20CF3027A5A3.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/2AB18AA5-9E9D-E811-9391-008CFA197BDC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3C89292C-9E9D-E811-A373-1866DA87A5A4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/522AA927-9E9D-E811-B0F8-0CC47A5FC2A5.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8884A63A-9E9D-E811-A96F-D4AE527F4A7B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/B20D6532-9E9D-E811-A55A-001E67E71943.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C00870A0-9E9D-E811-9241-24BE05CEADA1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D807EA28-9E9D-E811-BACE-28924A38DC1E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/DE7BFA2A-9E9D-E811-B291-0090FAA57B20.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E0BEE5C2-9E9D-E811-B858-001E67A401B3.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F0F8872C-9E9D-E811-A2DA-00266CFFBC74.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/FC47C02A-9E9D-E811-A824-FA163E74E86E.root',
] )
