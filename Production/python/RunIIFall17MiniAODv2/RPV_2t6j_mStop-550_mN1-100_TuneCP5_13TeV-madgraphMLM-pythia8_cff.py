import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/08A5CECA-95AC-E811-9E44-24BE05CEACA1.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/583F209E-95AC-E811-90EB-0025905C2CB8.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/5ACC569C-95AC-E811-9B0C-0090FAA575D0.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/64EC8B1E-96AC-E811-B753-14187764311A.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/96CA9C02-96AC-E811-9FE2-001E67E71DDA.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/A44063DB-95AC-E811-8890-D4AE528FF49B.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/D877AE40-98AC-E811-BB77-44A842B45218.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F4D5FD77-7CA9-E811-AD40-A4BF01125A90.root',
       '/store/mc/RunIIFall17MiniAODv2/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/80000/F68CC27C-27A9-E811-A32B-A4BF01158CF8.root',
] )
