import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/042FAFF9-91C0-E811-8BCB-0242AC1C0504.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/120000/A6C20B18-8CC0-E811-AEA1-0242AC1C0501.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/34516DB2-799C-E811-91E7-008CFAC91AB8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9808E1BE-799C-E811-8A70-D4AE526A05F2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E63FA7BE-799C-E811-9E94-5065F381A2F1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-600_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/60000/A41D802C-38AB-E811-8531-0242AC1C0502.root',
] )
