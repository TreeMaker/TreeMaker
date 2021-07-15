import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/pilot_106X_upgrade2018_realistic_v11_L1v1-v1/110000/59AD18D6-D833-4040-9222-6FC07AD6AA9D.root',
       '/store/mc/RunIISummer20UL18MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/pilot_106X_upgrade2018_realistic_v11_L1v1-v1/260000/DFE9DD99-B3F7-3A46-BFD0-9328F268830C.root',
] )
