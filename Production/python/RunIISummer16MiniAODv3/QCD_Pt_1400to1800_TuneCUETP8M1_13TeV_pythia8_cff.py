import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3476F5E9-5BE4-E811-B278-3417EBE2F4B1.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/4E7F43E5-DAE4-E811-983C-509A4C749119.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/B680C091-5CE4-E811-8A17-3417EBE6455E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D2B4945F-5BE4-E811-B7C5-509A4C74D077.root',
] )
