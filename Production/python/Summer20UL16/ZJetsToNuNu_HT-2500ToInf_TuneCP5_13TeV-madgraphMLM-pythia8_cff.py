import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/110000/075F9427-8E30-3C49-970D-F5CD6AC73FB4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/110000/B0EAFFAB-EF46-E54D-B918-FE179560F30D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/110000/F8132C80-6DD1-7A4D-9353-8E463CFB3DBE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/3C3F3CDA-ED1A-314C-A913-D68446497AA8.root',
] )
