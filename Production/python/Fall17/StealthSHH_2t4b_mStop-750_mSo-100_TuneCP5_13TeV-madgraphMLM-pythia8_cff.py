import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0CB6CDB6-069B-E811-ACFF-00266CFFBCFC.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/10ABB3CD-069B-E811-B53C-003048FFD734.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2E84F2B3-089B-E811-AEB2-B8CA3A70A410.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/3C934589-099B-E811-9D07-0025901D0C68.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4C58AA17-059B-E811-85C3-AC1F6B56762A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/582958D9-089B-E811-A16A-D067E5F91B8A.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/70FBDE6B-059B-E811-9760-E4115BE5F180.root',
       '/store/mc/RunIIFall17MiniAODv2/StealthSHH_2t4b_mStop-750_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/985A54A5-069B-E811-9BA6-001E67E6F783.root',
] )
