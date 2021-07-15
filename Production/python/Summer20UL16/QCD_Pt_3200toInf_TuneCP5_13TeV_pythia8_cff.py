import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/pilot_106X_mcRun2_asymptotic_v13-v1/110000/2AEF52B7-1B16-9643-B942-28349D008727.root',
] )
