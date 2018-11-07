import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/0ACBA40E-69BA-E811-9949-0425C5DE7BE4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/36E85715-6BBA-E811-A714-44A842B4CC8B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/4077A508-69BA-E811-9E6A-5065F3817281.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/4AD6D90B-69BA-E811-BEB3-509A4C84EA1B.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/62052F0B-69BA-E811-80EB-009C02AABB60.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/86C3B1E0-6ABA-E811-8E5D-7CD30AD08F08.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/8A8B4BD7-68BA-E811-A7D2-0025905C431C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/924E2EAC-68BA-E811-8BAD-0CC47A4D76D6.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/B673491A-69BA-E811-8D5A-008CFA064778.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/BA986057-46BA-E811-80C2-0025904C68DA.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/C85E69DA-68BA-E811-A849-A0369FD0B196.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/E6AAF8DB-68BA-E811-9F0A-001E67792702.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/EA9B73BC-68BA-E811-8771-0025907DE266.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/FC5CBCB4-68BA-E811-A25E-90B11C27F8B2.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/98B809E1-71BD-E811-99E3-B499BAAB31F6.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/C4C5C50B-8AC1-E811-A692-B499BAAC02CA.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-850_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/E62E845D-70C2-E811-A0A5-44A842CFC9BF.root',
] )
