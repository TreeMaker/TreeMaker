import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/20F0378B-F7D1-E811-8D59-0CC47A4C8EC8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/466DD7DE-F7D1-E811-B628-FA163EE59243.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/483072D2-F9D1-E811-A34A-44A842B4D8B1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/5A84366E-F7D1-E811-9237-B8CA3A70A5E8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/80090E87-F7D1-E811-AEBF-00266CFFC7E4.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/8414967C-F7D1-E811-8B88-48D539F3863E.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/B0FA1A68-F7D1-E811-9139-009C02AAB4C0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C2F81D7D-F7D1-E811-87B3-001EC9ADFC39.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/C45DEC64-CFD2-E811-AA14-0242AC1C0500.root',
] )
