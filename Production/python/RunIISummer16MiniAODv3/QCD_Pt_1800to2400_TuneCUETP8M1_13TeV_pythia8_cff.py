import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/1010000/2259AEFF-94E8-E811-9483-0025905C4474.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/32662D0C-8EE2-E811-AF38-70106F42AFF8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/4EC9C57B-D8DE-E811-A848-0025905C4474.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/BE743C23-BCDF-E811-A359-D0BF9C033BB0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/F63ED124-D9DE-E811-A3A3-0025905C42D4.root',
] )
