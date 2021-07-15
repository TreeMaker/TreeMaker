import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/39237E31-AEB1-3141-BA09-BFFF964A7A06.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/43CCDEB7-93C0-8447-9B51-CFBE3F110E67.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/846DAF02-F33D-0B4B-95C4-8F5F8DC25746.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/942BEA65-273B-434E-8F03-8A1F525463D3.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/C9B7A817-6AA0-4440-9628-3175583F468A.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/CA6069A7-7714-0A49-A2CB-57626D48D08C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/230000/DD075A54-9B2C-2442-87CC-2E5964B618CC.root',
] )
