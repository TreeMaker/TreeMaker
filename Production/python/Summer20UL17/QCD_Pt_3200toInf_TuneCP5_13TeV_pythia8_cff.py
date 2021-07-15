import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/pilot_106X_mc2017_realistic_v6-v1/110000/7C3BC802-91B0-8740-84A3-D306E2A30C67.root',
       '/store/mc/RunIISummer20UL17MiniAOD/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/pilot_106X_mc2017_realistic_v6-v1/270000/4E31FB96-8E4C-FB4B-A833-9C1A6550CAAE.root',
] )
