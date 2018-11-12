import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/42E74C6F-5ABE-E611-ABA0-7CD30AC030A2.root',
       '/store/mc/RunIISummer16MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/60C39B52-5BBE-E611-8D82-008CFAF558EE.root',
       '/store/mc/RunIISummer16MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CE219769-59BE-E611-BF71-0026B93F4C1B.root',
       '/store/mc/RunIISummer16MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D0FABDA4-5DBE-E611-B85E-782BCB206037.root',
       '/store/mc/RunIISummer16MiniAODv2/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D4947D01-5DBE-E611-81E4-001D09FDDF6C.root',
] )
