import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/1AD42407-7AF8-E911-8B1D-24BE05C68671.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/38FAB330-7DF8-E911-8A70-0CC47A5FBE21.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/3A0FCA33-7AF8-E911-AEDF-A4BF01283757.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/5039DD30-7AF8-E911-9A96-008CFAFBEFE8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/646DC43D-7AF8-E911-99EE-B4E10FA3213D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/AC889310-7AF8-E911-B1B3-0090FAA573B0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/AE9D394B-7DF8-E911-91B7-00266CFFC13C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C2B11C07-7AF8-E911-9704-20040FF469C0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/DCA97AF6-79F8-E911-B10F-D48564597C70.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1050_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/E469F50F-7DF8-E911-97AE-C45444922ADE.root',
] )
