import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E0508098-C77C-E811-93C3-0CC47A4D761A.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/EAAD3D26-CC7A-E811-968A-F01FAFE38177.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/FABEAC57-C77C-E811-A153-0CC47A78A33E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/2EF18BFB-C076-E811-A541-FA163E0624B4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/3894D25C-C176-E811-974F-0CC47A7452D0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/4E834652-C176-E811-868A-001E67792818.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/6A87805A-8C76-E811-BE40-00000086FE80.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/7A34CCF9-C076-E811-937C-1C6A7A26728B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/80E25BA1-C176-E811-9B59-44A842BFA93E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/AE69A506-C276-E811-8B3D-008CFA111224.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/BAEFD3A0-C176-E811-A5F5-A4BF010261D4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/BE526B7F-1C71-E811-A9DE-801844DEEFD8.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/E43C57F1-C176-E811-9475-141877411D77.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/30000/E44E1A7C-D972-E811-AB7B-0CC47A13D418.root',
] )
