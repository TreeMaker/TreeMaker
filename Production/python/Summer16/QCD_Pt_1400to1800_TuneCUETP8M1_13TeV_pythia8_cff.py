import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/021F2782-BEB1-E611-8581-0025905A48E4.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/289019BB-BAB1-E611-85AE-0CC47A4D76C0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2EC9B784-BEB1-E611-B7DE-0025905A60E0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/90574A80-CCB1-E611-964C-0CC47A4D764A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/BC17960F-BFB1-E611-9723-0CC47A4C8EEA.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/D283E295-BAB1-E611-9EFA-0CC47A78A4A0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/E0C50E83-BFB1-E611-9228-0025905B85D2.root',
] )
