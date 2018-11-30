import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/1C682E5C-1DBC-E811-9B2F-0090FAA58BF4.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/2EF439F0-7EBD-E811-B4F4-509A4C83EF80.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/8CABF091-DABC-E811-A7D8-A4BF0112E0A0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/8EA07FDC-14BC-E811-99C9-0025905C94D0.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/962AEAC0-09BE-E811-B0ED-90B11C0BD311.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/A6958FD0-66BD-E811-8EFF-48D539F3866E.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/AAD1320E-3BBE-E811-8493-0025905C42FE.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/AED9C73A-0CBB-E811-8393-06B30400009F.root',
       '/store/mc/RunIIFall17MiniAODv2/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/270000/CAFB8FC8-ECBE-E811-A6DD-0242AC1C0507.root',
] )
