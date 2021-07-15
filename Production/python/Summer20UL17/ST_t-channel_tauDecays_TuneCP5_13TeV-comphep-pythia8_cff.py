import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/17BE6F12-E17C-7540-A3B4-27CEE17F9BCE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/1CC638CF-818F-6745-A89A-9F62719E8059.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/4450D14F-F59A-2D4F-90C6-4170EDDA2D8C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/720EBAFD-1EB2-A543-8CBE-A39310BC15DE.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/7FFD6DBE-EE06-034E-AC6E-A38B1482B13C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/81235257-0901-DD46-BD42-6F55449DB371.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/AA7F605E-6ABA-7B41-BB5D-A27615D3C683.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/AFB119F1-F464-D743-A1D0-F6EC5428B818.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B1E46641-DB83-5446-85E2-D88D04BEC628.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/B8A1F2DB-CEA7-1D4C-8DA6-DC7B6386A05C.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/C40E72F6-15D8-3C4A-BA86-59AB9D9DE357.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/CAD21B82-5254-EF42-A619-28421536FBEB.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/DCF95978-F016-F942-A328-6C0E60D6B786.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/DEE379D4-040B-6A4F-80A1-7583A60CE2B8.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/E9952653-8741-FE44-A082-5482D9F1B21F.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F14057B2-A1A3-0943-9349-DED352110FCA.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F3B19632-8032-E04B-9D28-C628076831D1.root',
       '/store/mc/RunIISummer20UL17MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/270000/F92D98FE-6AB0-5D4E-AE34-CE0C4A838746.root',
] )
