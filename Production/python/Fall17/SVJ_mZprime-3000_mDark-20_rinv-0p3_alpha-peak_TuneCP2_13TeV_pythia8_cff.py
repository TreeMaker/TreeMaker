import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/18AF4F2D-AD6E-E911-852A-0CC47AF9B302.root',
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/3E088621-F76B-E911-B5C4-B49691386D00.root',
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/3E5C0376-496C-E911-BEE5-0025905A6138.root',
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/9C033B3A-EE6B-E911-9A87-5065F37D4131.root',
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/9C804954-EE6B-E911-835D-0CC47A57CE00.root',
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/AC2B21B7-EE6B-E911-8271-F4E9D4A36760.root',
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/D4BDC8C8-EE6B-E911-B6EF-6C3BE5B5A038.root',
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/E07C4B6D-9E6A-E911-82C8-1866DA7F9780.root',
       '/store/mc/RunIIFall17MiniAODv2/SVJ_mZprime-3000_mDark-20_rinv-0p3_alpha-peak_TuneCP2_13TeV_pythia8/MINIAODSIM/PU2017_12Apr2018_DMinvis_94X_mc2017_realistic_v14-v1/260000/E86D5451-EE6B-E911-A13B-90B11C2AA388.root',
] )
