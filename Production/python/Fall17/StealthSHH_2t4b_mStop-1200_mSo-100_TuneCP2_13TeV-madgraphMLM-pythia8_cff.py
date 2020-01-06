import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/1865D700-6FFA-E911-83DD-1418776375C9.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/2059BF16-D4FA-E911-819B-14187741278B.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/5C5287E2-F2F9-E911-B148-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/6493247E-7FFA-E911-B61A-EC0D9A8221DE.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/66F9EA94-C1FA-E911-A824-28924A33AF26.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/8E4F745A-90FA-E911-B354-0CC47AA992C8.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-1200_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/230000/D4CAFC47-90FA-E911-AF27-0CC47AFF24CA.root',
] )
