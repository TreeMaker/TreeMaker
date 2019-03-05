import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/425CEE29-80AC-E811-AF85-001E67504685.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/4E5AF92D-80AC-E811-85A2-0CC47A1DF806.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/78577D1E-80AC-E811-AD3C-E0071B7A18F0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/7E78D544-80AC-E811-9FE1-A0369FE2C05C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/A6CC7E6F-80AC-E811-8BD1-A4BF0112BC72.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/D0F46E50-80AC-E811-B334-00259029E670.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/E22CF6B0-80AC-E811-AB4B-0025904B7C24.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F088EDB9-84AC-E811-816F-44A842CF060D.root',
] )
