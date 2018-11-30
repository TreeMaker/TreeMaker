import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/001CEA5F-72C9-E811-BA66-00259029E84C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2CD7E036-72C9-E811-B8BC-B499BAAC0572.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4A60530E-72C9-E811-9AC1-1866DA879ED8.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5A6EF34A-72C9-E811-B5F2-001E67DDC051.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/D8371BB4-7DC7-E811-B485-002590D9D8AE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/1ED8C138-4BBB-E811-B449-246E96D10C24.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/2C39513A-4BBB-E811-A565-F02FA768CFE4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/30571216-4BBB-E811-AD1A-0CC47A0AD476.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/42FFEC30-4BBB-E811-81B7-001E67397003.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/58987AEF-4ABB-E811-BFD6-E0071B6C9DF0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/5E81430E-5CBA-E811-9AE8-002590D9D8AE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/60152222-4BBB-E811-AD87-0CC47AD990C4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/6A2711BC-4BBB-E811-88C7-0026B92786AC.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/90B7CF6A-4BBB-E811-A85C-1866DAEB1FC8.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/D6F1494D-4BBB-E811-8551-7CD30ACE1B58.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/F48D6DF7-4ABB-E811-8D2F-0CC47A7C3424.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-1200_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/D0903CAD-F5C5-E811-80BC-002590D9D8C4.root',
] )
