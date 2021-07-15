import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/1A917548-04B7-1843-8065-B52266E99B2C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/2715905F-1D3F-1643-9E34-8E92578FAB24.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/2E7D47B6-B76E-E14B-9FB7-105F892D01C6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/3CDE9D7C-DF75-7A4E-A415-D28CC548F335.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/4E360DBE-158F-D244-9730-2777E6718612.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/4E583976-0C8D-4C40-A506-9CD5A222ED62.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/52A73170-8870-2047-A149-3AAEF42F68F1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/5A878C1F-28B2-F648-9684-4CFB033D43B1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/606B2B06-3FE2-9B44-88A1-12ED79464051.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/72343BAF-4DCD-534F-BFF0-4E41B9F88F97.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/742EE824-7D0B-9442-AB92-3633584CD734.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/79691D8A-D7D0-764E-8F1C-7270D2DB9E5E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/79D28705-80EC-2345-B17D-EE6850A5B925.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/88F99412-902D-094E-8B1A-1805BB1E4202.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/91FD2A69-FFF9-C745-9749-8261901B50D0.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/A1B9234B-0DC7-BF4A-9387-8F10815012B9.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/BB3FEFE7-1A69-5448-98B1-49E90A5E15C6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/CD976356-3DC6-DB45-AF54-ADCCB364998E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/EBC220FD-CDDF-3640-B929-6B1B93DB0ECA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/F0DCC267-D939-FA4C-A469-1D06AA7CB158.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/F2DE6248-FF04-E74D-B826-348C60925305.root',
] )
