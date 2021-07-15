import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/1BC0D0F5-34E1-3F47-A51F-D86BB9205EF6.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/1DFECE77-B679-3540-9F04-24200D4F0F38.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/65C65CE2-273B-AF44-82FF-9EE8EBC48C98.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/717679BA-B258-4242-A5C3-BBFF7A87C6DC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/95C3E85A-382A-5947-8E77-0ECB4041F339.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/AC3DD55D-127F-464E-9887-74B75F2F97BC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_tauDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/DEF8DBE6-F834-0447-9B83-5CBD194ED8D8.root',
] )
