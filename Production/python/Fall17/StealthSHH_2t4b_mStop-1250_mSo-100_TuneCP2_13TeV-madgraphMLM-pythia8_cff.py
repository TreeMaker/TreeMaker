import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0080FBB1-7908-EA11-92A8-002590D6012E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/20E724C0-7908-EA11-A670-38EAA78D8ACC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/26D2673C-7908-EA11-87D8-782BCB20F90E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2EF6136C-7B08-EA11-90FE-3CFDFE63D300.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/AA9A351C-7A08-EA11-ACC9-0CC47A206FCC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1250_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/C87FC2AF-7908-EA11-BEEA-98039B3B003A.root',
] )
