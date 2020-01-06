import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/02CF5D41-1C0F-EA11-84C9-0CC47A78A3D8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0C09552E-1C0F-EA11-B45F-002590DE38C8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0CFC3EC4-A7FC-E911-A1C6-0025904CF972.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/221D4375-EEFB-E911-9A6B-AC1F6B23C834.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/46E50800-F2FC-E911-BB6C-B4E10FA3213D.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5CB95825-1C0F-EA11-9B54-1866DAEA8394.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/668CE844-1C0F-EA11-AF69-68CC6EA5BD22.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/84A813E5-7CFE-E911-AD48-AC1F6B23C80A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D49B58D0-1B0F-EA11-9B95-0025905C2CE8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D4D5CB5E-B1FC-E911-8574-AC1F6B23C848.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E4F2360B-0FFB-E911-AE69-0CC47A54529A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F663FE3A-1C0F-EA11-8BE7-AC1F6B23C93C.root',
] )
