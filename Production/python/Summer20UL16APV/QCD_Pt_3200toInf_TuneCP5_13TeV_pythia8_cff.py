import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/pilot_106X_mcRun2_asymptotic_preVFP_v8-v1/110000/566DFB03-F583-EF4F-AD26-9CAE984A6BAA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/MINIAODSIM/pilot_106X_mcRun2_asymptotic_preVFP_v8-v1/260000/DE5BDC44-88A5-6744-A8F2-1BEDF6935DA5.root',
] )
