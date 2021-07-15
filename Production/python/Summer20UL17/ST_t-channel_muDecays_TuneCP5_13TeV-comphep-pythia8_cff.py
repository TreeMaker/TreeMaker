import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/0D6D5019-FF42-A247-9A82-C0CBEF549A33.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/0F2057F8-DE26-A642-B320-AEFC7CD05BEA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/16220F66-7778-1F4D-933A-8A23558796BD.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/2510551A-2B41-D545-88E9-BE4B479DAA0F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/3C646BD8-F670-6A4F-84D4-5D1A18E5B0EC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/4ED6915C-A0F2-9142-BF4C-AF245F118BAC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/6B32F8BA-5D7A-8E45-87BE-DF5FBBD7E2C4.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/716E279A-8449-E643-8184-3A3C5F140220.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/71C4E98A-8EDD-7C49-99B7-4D138BF78F4E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/7AFA5937-35CF-6448-B4EB-E7BCEC8F92BC.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/857A81D4-AD74-F547-ACCA-03013BD9D1E6.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/88A15307-803E-3E4D-BCA8-5364868F1AB2.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/A2BE5BCE-DC70-A94B-979D-624D01C57729.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/A2EB0E45-D328-3349-8563-490394016CB5.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/BD288DF5-94EF-7E4D-BE71-74CC2EAE6892.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/C3A84C6D-9392-264F-8897-32D55A0F9337.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/D267E03E-2804-D64F-A0E7-F8FE81FDC54F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/D5ED1939-2727-F946-9FD6-414C2F8564F8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/E1F850DA-C390-934A-A341-AAB01BEE623E.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/250000/E5874E72-F0E5-8A43-88D3-F84FB772CB33.root',
] )
