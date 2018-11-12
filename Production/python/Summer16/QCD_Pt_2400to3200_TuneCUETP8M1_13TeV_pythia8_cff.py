import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/060A4CEC-A4B1-E611-921A-0CC47A7C3434.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/1226943C-ADB1-E611-8AED-0CC47A4D7606.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/188C9E15-A4B1-E611-A9A3-0025905B858E.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/2671BBBE-A9B1-E611-B23B-0CC47A78A478.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/4C13A293-B7B1-E611-A6B3-0CC47A4D7674.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/68AADDAE-B7B1-E611-95BD-0025905A60E0.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/6E9A403D-ADB1-E611-A80E-0CC47A4C8E8A.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/8CC2386F-A6B1-E611-AFDF-0CC47A4D7604.root',
       '/store/mc/RunIISummer16MiniAODv2/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/110000/96A1ACA4-AAB1-E611-81F6-0025905B8574.root',
] )
