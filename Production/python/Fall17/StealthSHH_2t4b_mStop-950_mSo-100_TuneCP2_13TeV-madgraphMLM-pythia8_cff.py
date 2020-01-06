import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/36F57A72-BCFD-E911-91C0-549F358EB748.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5CBD1CFE-7E06-EA11-832D-0CC47A7C34C8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/60D76FF5-D2F9-E911-8320-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/AE269565-56FD-E911-85F0-FA163E50D9CE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-950_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/BAD3C58D-BCFD-E911-8C4B-00259075D706.root',
] )
