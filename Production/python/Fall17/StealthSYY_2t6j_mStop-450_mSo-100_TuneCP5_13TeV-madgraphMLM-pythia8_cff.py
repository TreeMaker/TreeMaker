import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1033042D-369D-E811-9833-008CFA197AC4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2C05B497-4C9C-E811-9CA2-FA163EBD80DA.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3E3B6F27-369D-E811-99AD-24BE05CEADA1.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/42DF6D33-709C-E811-AF9E-003048FFD734.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4A62D751-729B-E811-A418-0CC47A4C8E26.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4C0CF432-039D-E811-B86B-0CC47A4D7692.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4C8C5883-C59B-E811-96A6-0CC47A4C8F0C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5E49DE4E-839A-E811-9B1A-0025905A60E4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/6EF1277C-359B-E811-87CA-0025905A60D6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7422646F-369D-E811-92BE-003048FFD722.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/B072BE3D-369D-E811-A757-0025904C66A4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/C6CB543B-C79A-E811-AFAC-0CC47A7C3408.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D632075C-D59C-E811-AEF3-0025905B85B8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/EA7318A3-069B-E811-BE36-0CC47A4C8E3C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/FE5D4C0D-369D-E811-91F1-FA163E399D3B.root',
] )
