import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/0477D0C7-09D4-E911-9D99-FA163E38D54A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/0C452E8F-18CA-E911-B91F-E0071B6CAD00.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/4458AE6D-10C9-E911-9C2C-0CC47A4D7650.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/64CCFEA7-63CA-E911-878C-FA163EF23386.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/96CC7C8E-18CA-E911-87EB-A0369FC51BB8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/F877069D-18CA-E911-96BE-24B6FDFFBC48.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/270000/FA70847E-18CA-E911-8003-009C02AAB4C0.root',
] )
