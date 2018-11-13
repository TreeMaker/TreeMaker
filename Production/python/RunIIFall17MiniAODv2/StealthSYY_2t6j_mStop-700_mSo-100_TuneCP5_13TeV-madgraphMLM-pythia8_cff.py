import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/270000/285414D6-D3C6-E811-9D38-001E67581344.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/0643F0CD-50C7-E811-85B4-002590E2DA08.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/4014D3A3-55C7-E811-993D-E0071B7A4550.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/507764E5-50C7-E811-B908-001E67E6F5AD.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/828CFE35-51C7-E811-95FE-0CC47A4DEDD2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/BA00F76D-51C7-E811-99CC-00266CFFBC64.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/BC42C425-51C7-E811-885E-008CFAF75512.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/BC664C47-51C7-E811-B3E9-002590D8C724.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/DC88092A-51C7-E811-87A6-0CC47AF9B51A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/90000/986FB508-48A8-E811-9536-002590D4FC5C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/90000/9E4D6FE7-7AA8-E811-917A-0025901FB438.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/90000/C2B5748D-48A8-E811-A59C-A0369F3102F6.root',
] )
