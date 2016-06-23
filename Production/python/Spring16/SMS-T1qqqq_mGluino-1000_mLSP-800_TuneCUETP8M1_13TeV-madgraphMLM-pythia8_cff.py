import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/0694055B-FB35-E611-AEC0-001E67A3FEAC.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/10C71B3A-3637-E611-9838-008CFA0A56F0.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/42995EB7-E635-E611-9C90-001517FAAC78.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/B642EB5F-0A38-E611-89C0-0025905B858C.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/BAE83A6A-0B38-E611-BF40-0025905B85DA.root',
       '/store/mc/RunIISpring16MiniAODv2/SMS-T1qqqq_mGluino-1000_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v2/80000/C62B218B-CF36-E611-9018-001E67A40604.root',
] )
