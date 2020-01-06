import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/08F5689D-CA09-EA11-9387-001E67E5EAF0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/14BF67AF-CA09-EA11-85E0-0CC47A4D7630.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1A9B8BD6-CA09-EA11-A68C-D4AE529013D2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2CD59EEA-CA09-EA11-A0E8-0CC47AF97126.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/3AB7BFE3-CA09-EA11-9594-0CC47AB6503C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/4A022295-CA09-EA11-8037-0025905746C8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/54D42583-CA09-EA11-8AC9-0CC47A7E6820.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B0A26794-CA09-EA11-9FB2-5065F37D7121.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/C03099FB-CA09-EA11-8051-002590FD030A.root',
] )
