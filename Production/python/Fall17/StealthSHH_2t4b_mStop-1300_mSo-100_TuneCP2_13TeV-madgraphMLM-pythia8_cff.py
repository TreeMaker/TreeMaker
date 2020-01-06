import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/10E58DFA-A3FC-E911-BE30-B49691091EA2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/26F5D48A-8EFB-E911-B9C1-008CFA197CA4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/2E1DBC57-E2FF-E911-8086-782BCB53A3A4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/6A86DD79-A3FB-E911-9838-0CC47AFCC686.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/7050653F-CBFC-E911-B312-0CC47A1DF7E4.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/7E68263F-77FB-E911-88C2-6CC2173D5F20.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/B8C6D170-8EFB-E911-9FA8-34E6D7BDDECE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1300_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C40C152E-E2FF-E911-88E0-24BE05C4D8C1.root',
] )
