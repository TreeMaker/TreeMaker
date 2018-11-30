import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_12Apr2018_94X_mc2017_realistic_v14-v1/120000/105AF6F2-52EC-E811-8633-A0369FD0B170.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_12Apr2018_94X_mc2017_realistic_v14-v1/120000/1CFFBF5E-35EC-E811-89BE-48FD8E282493.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_12Apr2018_94X_mc2017_realistic_v14-v1/120000/22BDE73F-63EC-E811-87B0-AC1F6B0DE33E.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_12Apr2018_94X_mc2017_realistic_v14-v1/120000/3C25621D-2AEC-E811-B90F-A0369FD0B38E.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_12Apr2018_94X_mc2017_realistic_v14-v1/120000/708E6AE5-43EC-E811-95A8-48FD8EE739EB.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_12Apr2018_94X_mc2017_realistic_v14-v1/120000/7C3966C6-23EC-E811-9F0C-AC1F6B0DE13A.root',
       '/store/mc/RunIIFall17MiniAODv2/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/MINIAODSIM/NoPU_12Apr2018_94X_mc2017_realistic_v14-v1/120000/8E2EAECA-66EC-E811-8C3B-A0369FD0B316.root',
] )
