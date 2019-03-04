import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/32F17ABD-FF22-6B47-A4A6-78D1248A548F.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/4107CDD4-D1A9-8041-AB77-0A010790CEDF.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/42DA49D9-4F0B-DD41-91B6-F2FF10374EFE.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/4848E12C-F2E1-624D-90E3-ADE0DD332995.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/61C945A1-4769-8748-8F40-AC37C6833133.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/7E57252B-4422-E44F-A1A8-62B9F077B19A.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/ACBE235F-993F-F841-A699-AFABCBCBFA8D.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/C5579E6A-B196-F945-BA70-24B63710BD64.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/DBAF10DF-289B-394D-A1AC-132101043BD5.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/F061F93B-72DA-864B-A703-21228F937CF8.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/F4953B6B-A172-6242-B828-F803C0071AAE.root',
       '/store/mc/RunIIAutumn18MiniAOD/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/100000/FB6134EC-A899-E248-A49C-ADD8649A91C4.root',
] )
