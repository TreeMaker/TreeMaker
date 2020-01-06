import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/20F08A0D-BD08-EA11-BAE6-1418774A265B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/3E4F2ED9-BC08-EA11-9A40-24BE05CE1E11.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8E22B236-BD08-EA11-BBB3-D485646062F2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/BEF41A1C-BD08-EA11-B48E-001C23BEDBA7.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/DAB35029-BD08-EA11-B904-A4BF01287D43.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/ECBA07F0-BC08-EA11-9BF6-003048F5ADEC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-850_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/FA004298-BD08-EA11-BEEA-0CC47AB58BE4.root',
] )
