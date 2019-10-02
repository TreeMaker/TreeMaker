import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/044F4C49-3AC9-E911-BAC9-0CC47A4D7674.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/0E52B9DC-FDCA-E911-A8AE-0025905C2CBE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/12BCC0B0-83C9-E911-9395-484D7E8DF0C6.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/26BF4BA9-02C9-E911-9E19-0CC47A7452D0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/326EFDD0-A5C8-E911-85DC-00266CFE797C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/3E4E6B77-5DCA-E911-8A39-7CD30ACE160C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/5AD14086-89CA-E911-946B-FA163E5EE8B3.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/628222EF-5DCA-E911-AE9E-28924A33B9AA.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/981509B4-A3C9-E911-955B-3417EBE51E38.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/AAFD3E13-42C9-E911-B213-008CFA197EB0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/B89C628F-5DCA-E911-A05A-D48564593FA8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/DE951485-46CA-E911-8BDC-7CD30ACE1684.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/E654F5BF-63CA-E911-BDAE-FA163EC44FA9.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/E8E25924-BFCA-E911-B69D-A0369FD0B374.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/EA7B14BC-63CA-E911-9A42-FA163E0A6472.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-450_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/FA44172D-76CA-E911-BA6C-F4E9D4AF7940.root',
] )
