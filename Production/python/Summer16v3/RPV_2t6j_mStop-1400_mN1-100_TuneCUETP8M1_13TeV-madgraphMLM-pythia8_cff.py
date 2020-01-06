import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1400_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/40A86B41-48FA-E911-9325-008CFA111154.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1400_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/584094FF-4CFA-E911-8550-A4BF0102A5BD.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1400_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/80773DC9-5CFA-E911-95B9-0CC47AF9B2E2.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1400_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/BC362702-49FA-E911-A89E-6CC2173C9150.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1400_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/C8603981-1DFA-E911-B3F1-FA163EC97030.root',
       '/store/mc/RunIISummer16MiniAODv3/RPV_2t6j_mStop-1400_mN1-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/240000/F2832208-91FB-E911-AAC0-0CC47A4D765A.root',
] )
