import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/028EA5F9-61C0-E811-9C91-848F69FD86EA.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/5895938A-62C0-E811-A273-009C02AABB60.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/7642AEF5-61C0-E811-B3C8-782BCB38F205.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/AE9788ED-61C0-E811-8263-008CFAE45054.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/B4377898-62C0-E811-828C-68CC6EA5BDF2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/C290DCD2-61C0-E811-A9EA-0CC47A4D75EE.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/C4239CF1-61C0-E811-A83E-E0071B74AC10.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/D6A186F4-61C0-E811-9323-0CC47AA992AC.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-700_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/DEB642F8-61C0-E811-8D2D-0CC47AFC3CA0.root',
] )
