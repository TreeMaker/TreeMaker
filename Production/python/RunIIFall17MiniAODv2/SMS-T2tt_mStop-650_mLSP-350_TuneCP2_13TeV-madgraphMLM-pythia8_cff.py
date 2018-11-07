import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/92D57083-5AC8-E811-9753-3417EBE47FE5.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/A24E8B44-5AC8-E811-9E64-F04DA275407C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/D0862608-6DC8-E811-B988-001E67E71368.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/12A08847-74BA-E811-978E-509A4C84547F.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/20ECA680-72BA-E811-B16F-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/2649397C-72BA-E811-BE64-7CD30AD0A78C.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/3254A869-72BA-E811-89AC-48FD8E282473.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A8070C7D-72BA-E811-BF45-6CC2173C3E80.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/BCF23581-72BA-E811-868E-90E2BACBAB00.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/BE54279F-72BA-E811-AEFD-001E67E69DEC.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/CE5BD98A-72BA-E811-ADD5-A0369F5BE308.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/D235E082-72BA-E811-816B-901B0E6459CE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T2tt_mStop-650_mLSP-350_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/DA406F63-72BA-E811-9D4A-0025905C43EA.root',
] )
