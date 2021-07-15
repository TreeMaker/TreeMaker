import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/03BB2521-5327-034D-8AD3-8853D0CE4BD8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/1A203148-52DA-B44C-9A43-5D53217C85B7.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/407BF4F3-EC7C-5D43-8CE6-13FEAE91097B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/551E8608-A317-A44C-80C5-BFC17360AC3B.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/574DA2B6-BA53-9643-AC37-ABFBE8A5B77A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/84B00FD6-BE41-4142-9D59-8F71D80A1062.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_eleDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/A7166196-55D7-F847-AD25-05A6ED492E5E.root',
] )
