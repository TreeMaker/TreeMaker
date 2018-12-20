import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/0423C306-71EF-E811-A586-008CFA197CA0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/54504C6E-71EF-E811-BEC1-008CFA0646CC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T5qqqqZH-mGluino1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/80000/9064D53A-71EF-E811-9512-008CFA1974AC.root',
] )
