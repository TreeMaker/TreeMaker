import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/0263972E-86F9-E911-B3B4-D8D385AF8994.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/22AC5405-ACF9-E911-8E24-AC1F6BC67D4E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/6883E0D8-A7F9-E911-A4DD-24BE05C48801.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/880227DB-74F9-E911-827A-F0D4E2E523A4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A40638BC-6BFA-E911-89CB-509A4C838C16.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A8E6ECA6-70F9-E911-A742-008CFA0518D4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/B0D938CF-74F9-E911-B69D-00266CFBE29C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C01B93B4-05FA-E911-B03F-0CC47AFF01F0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSYY_2t6j_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/D031895B-70F9-E911-885A-28924A38DC1E.root',
] )
