import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1200206A-8EF8-E911-8781-0CC47AB64FB2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1210ECD5-68F9-E911-9938-0CC47AE0F33C.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/18EC85B7-E302-EA11-ADEB-0025905D1CB6.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/18EF1D1F-82F8-E911-AF67-0025904B300A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/265B4A9B-E602-EA11-8937-008CFA0A55E8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/28AED293-E302-EA11-94ED-90B11CBCFF41.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/40802E8F-E302-EA11-A6FB-001E675A4759.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/8A46D815-E402-EA11-80B0-FA163E2597D0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/AC37879A-E302-EA11-968B-0CC47A0AD780.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/B81692D9-3003-EA11-B318-AC1F6B23C592.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/C6D7731B-1103-EA11-9D62-44A842CF0634.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-600_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/E8833102-E502-EA11-9229-E0071B7A7870.root',
] )
