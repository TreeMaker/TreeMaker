import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/0B674E58-7AE7-A248-A1F3-0A0CA2590022.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/0E571CF5-8A99-3843-8B26-993529EADC27.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/4847829E-4D9E-B44A-832F-C5FDF910C239.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/6D1BC419-4447-1747-9C7E-231AE504C5AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/8CB93CA8-0AA2-644D-91A8-6FA61EBE6B8B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/984943A0-9E8E-3347-8140-297B8DBF2429.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/ACBEF60A-A986-504F-82E9-967AB4336360.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/B699EB37-2137-F143-91AE-394DF85FB6A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/DE645D01-12D2-FC44-8580-E31B17BE37B4.root',
] )
