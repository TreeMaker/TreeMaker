import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/0E03A042-6ED1-E811-BFC9-008CFA11113C.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/144CBF88-94D3-E811-9AC3-00259055C836.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/246E347D-94D3-E811-A3D1-3417EBE47FE5.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/46FA408B-94D3-E811-86F2-0CC47AD99146.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/6284F17F-94D3-E811-9204-0CC47AFC3CA2.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/70F23E84-94D3-E811-B3DB-E0071B7A9810.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/9062687F-94D3-E811-AAD8-48FD8EE739BB.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/A8BFCA2E-6ED2-E811-8EB8-008CFA165F40.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/AABBB3B2-63D1-E811-A253-008CFA165F44.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/110000/C8F6BB82-87D1-E811-8E0A-008CFA580778.root',
] )
