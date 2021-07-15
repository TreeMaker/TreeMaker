import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/1877FDA5-17A4-EB4C-B5C2-44E0B2B66A53.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/201B1F63-5F74-7441-AB29-F1E90D9ECD50.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/361E95F3-FA7E-5245-8145-9A0A9BD4B670.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/5EDF8603-6CA9-3249-8712-71BFEEF98CD5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/902A3FF8-6B3B-7046-9542-66BC2ECB02E5.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/BE2EA98B-9276-1E4F-9F8D-DD0261B37AE2.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D5AFB4E7-47CF-9547-933C-9AD0C5690CDF.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ST_t-channel_muDecays_TuneCP5_13TeV-comphep-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/D6A3021D-8559-7740-BA9C-B2251AFD10D9.root',
] )
