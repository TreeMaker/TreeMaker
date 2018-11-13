import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/184D9B11-ED98-E811-91E8-A4BF0112E2C8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2091FF1A-ED98-E811-8D12-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3EAECFEF-EE98-E811-8CC7-44A842CFC9CC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/48640CEE-EE98-E811-84C6-3417EBE705CD.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/52C8A8AB-EA98-E811-9584-E0071B7AC5D0.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/548E5615-ED98-E811-BF58-0025905D1E0A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/621861D3-EB98-E811-9AD2-A0369F8363F2.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8A564DB9-EA98-E811-B694-782BCB539A7E.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/F83E4119-EB98-E811-B20B-0CC47A5FC619.root',
] )
