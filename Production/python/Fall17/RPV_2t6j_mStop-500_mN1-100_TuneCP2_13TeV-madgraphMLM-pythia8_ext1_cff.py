import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/0410116B-5DCC-E911-A7A7-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/12538BEC-5DCA-E911-A001-A0369FC5EEF4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/3CBFB5EE-63CA-E911-88C6-FA163E2301A5.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/60DD2FFC-5DCA-E911-8A0E-008CFAF06618.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/6A7534DB-04CB-E911-B0BD-0CC47AFF24C6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/86E50C62-60CA-E911-B5B5-0CC47A7C34D0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/9887BB0A-64CA-E911-82B2-FA163E551BC0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/9ECB9806-64CA-E911-8AF8-FA163E4A5537.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/CCD59070-6ACA-E911-9DFD-FA163E7D2612.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/D4CC5D7A-5DCA-E911-8E5E-008CFAF72B30.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/FE93B9F0-5DCA-E911-A741-44A842CFCA1A.root',
] )
