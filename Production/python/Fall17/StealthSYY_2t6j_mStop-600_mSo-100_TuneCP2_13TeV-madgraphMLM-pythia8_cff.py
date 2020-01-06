import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/52E61C8A-2208-EA11-A3A3-0CC47A7C34A0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/58E22D0D-2308-EA11-99FC-20040FE9CBB8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/6062F003-2308-EA11-B946-0CC47A5FC281.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8880EC46-7BEE-E911-8A27-3417EBE70684.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9E133A5C-2308-EA11-9274-FA163E7E402D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B044E49C-32EE-E911-B168-FA163ED3779B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/C035D725-2308-EA11-8463-002590D60056.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D2BDE711-2308-EA11-B050-509A4C838C3E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E4DDEB2E-FEED-E911-88E2-FA163E57DB33.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/EAA47921-2308-EA11-B69C-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FC09DA67-2308-EA11-98D9-A0369F30FFD2.root',
] )
