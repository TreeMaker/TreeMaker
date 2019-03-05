import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/CC8A5A46-9EC0-E811-86F0-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3E26204A-879C-E811-BFA8-0025905B860C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/440B6650-879C-E811-9F2E-00266CFFCCBC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/6062D950-879C-E811-BF08-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/98EF8949-879C-E811-B1EC-5065F381A2F1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-800_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/FAB27A42-879C-E811-A5F1-002481DE4BFC.root',
] )
