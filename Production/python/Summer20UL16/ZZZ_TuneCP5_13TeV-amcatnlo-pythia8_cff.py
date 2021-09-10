import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/0BD1D957-D2BA-2A40-B3D3-AA4230AF4C3C.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/6FEFC983-493B-AF48-A6FB-D90FDD5BE759.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/80A664E5-1649-7744-A06B-F0532C255EA3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/9C58BE54-17E6-6343-889A-E3AF58349FFF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7A23DC04-74EA-284B-B4D5-63F0357634C5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/F1FFC265-F9D9-D344-A71F-DAA550EF1089.root',
] )
