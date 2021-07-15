import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/35AA20A3-58F7-5B47-90FE-3C5719DC039A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/40DA2334-95E2-7348-AB65-9B853EA8DEA6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/40E6D3A0-1662-A44B-AEDB-823C9C0359AE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/7BE8044D-452F-2649-B225-64DD233A547C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/A48EC47A-5EFE-8B47-9D55-C6AAE1B5D3CA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/AA21FFC3-49D4-114B-9AE9-B6A5D3E8277A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/F577A287-C2BA-054C-BE49-BC482B19D148.root',
       '/store/mc/RunIISummer20UL16MiniAODAPV/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v8-v2/00000/F58DE258-E669-4B48-ADBE-421028EC5FA9.root',
] )
