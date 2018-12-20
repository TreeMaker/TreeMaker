import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/12CA946D-BAE5-E811-8E02-D4AE5269F611.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2C852F75-25E5-E811-A965-782BCB161FC2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/68920335-25E5-E811-A0D5-1866DA890969.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C65717F0-23E5-E811-B344-D4AE526A109A.root',
] )
