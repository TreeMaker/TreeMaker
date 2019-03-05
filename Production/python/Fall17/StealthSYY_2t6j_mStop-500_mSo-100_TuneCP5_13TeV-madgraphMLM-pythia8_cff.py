import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/0C140715-509D-E811-A7C8-0242AC1C0503.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/1ED704EC-4B9D-E811-9DFC-00266CFF0608.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/2419D0BF-4B9D-E811-949D-A4BF0115970C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3662F61A-4C9D-E811-A11E-B083FED42A6D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/38F668F9-4B9D-E811-AEA5-0025904A91F6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3E71A1EF-4B9D-E811-958A-008CFA197E10.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4A04E9EF-4B9D-E811-A9FF-90B11C248E7B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4A8FB3F4-4B9D-E811-91B9-0CC47A5FC619.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/88E49F77-FE9C-E811-9493-001E677926C4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/924EBAF0-4B9D-E811-92F8-001E67A3EBD8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/BE5A84E4-4B9D-E811-8B5A-0025905D1CB6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D6A6C9BF-FE9C-E811-A712-24BE05C63741.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/EC0E84E4-4B9D-E811-83A6-24BE05CEDCD1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F218881D-2C9D-E811-8879-0026B9278644.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/FC9BD5F5-4B9D-E811-BBAB-0025905A6084.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8623D657-53A9-E811-AEE8-0CC47A7452DA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E8D4C788-54A9-E811-8B72-EC0D9A0B3340.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/410000/701D1B3A-B3A7-E811-AC21-509A4C84543E.root',
] )
