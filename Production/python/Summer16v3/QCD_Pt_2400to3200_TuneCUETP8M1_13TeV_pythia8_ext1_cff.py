import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/08E0F789-9BE2-E811-8498-48FD8EE73ABD.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6CD391EA-95E1-E811-B4FC-48FD8E282499.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/6EA405A4-9AE1-E811-A68D-48FD8E2824B3.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/8E27E481-9AE1-E811-BBFC-48FD8EE73A69.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/A6614D2E-9CE1-E811-A723-48FD8EE739A9.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/D0AE11FE-A4E1-E811-9F9C-48FD8EE73AC5.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/100000/FC7A0380-A2E1-E811-B868-AC1F6B0DE290.root',
] )
