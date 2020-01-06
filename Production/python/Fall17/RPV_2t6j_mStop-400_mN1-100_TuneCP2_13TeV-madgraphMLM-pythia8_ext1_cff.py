import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/1E16CF42-87E7-E911-A14C-0425C5DE7BE4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/26AF90AC-06C9-E911-AE53-0CC47A745284.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/286F4839-87E7-E911-A871-44A842B298F1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/3A0067A4-63CA-E911-A606-FA163E3B61E2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/3A7B7ECB-63CA-E911-9958-FA163E8A2455.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/5A1E7D00-87E7-E911-A818-24BE05CEEB31.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/5ACC2833-87E7-E911-8B0C-44A842CFD626.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/5C642C49-64CA-E911-9CFD-FA163EA17E34.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/6880485B-87E7-E911-9916-0CC47A4C8E8A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/7E45B47D-87E7-E911-8575-FA163EB14403.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/849146C6-63CA-E911-BEAD-FA163ED917B4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/86A87A47-87E7-E911-AC1A-BC305B390AA7.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/AE2CB9DE-63CA-E911-A45B-FA163E3966FF.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/B682BC37-87E7-E911-942A-ECB1D79E5C40.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/C25E05E3-63CA-E911-BD61-FA163EF73E73.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/D06B0450-64CA-E911-9025-FA163E5F18A2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/D20C3B63-87E7-E911-9393-7CD30AD096B8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/D2D6C78B-D5C9-E911-AC31-008CFA197D10.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/ECD2617B-0BE0-E911-9610-008CFA1C907C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-400_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/F680F8AD-63CA-E911-924B-FA163E80893D.root',
] )
