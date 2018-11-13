import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/1473013D-CACB-E811-A36B-1866DA85D967.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/184552B2-A6CB-E811-8A76-008CFA1CBB34.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5E9B5A5E-B0CB-E811-8DC9-EC0D9A822616.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7C6B376E-CBCB-E811-8D16-1CB72C1B2D88.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7CE6798E-CCCE-E811-A723-008CFAC94230.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/84001DA3-AFCB-E811-8E0B-A4BF01013D12.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/A06996AE-A5CB-E811-8CC5-3417EBE64B85.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-750_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/EEF59FB3-9ECB-E811-8746-0242AC1C0504.root',
] )
