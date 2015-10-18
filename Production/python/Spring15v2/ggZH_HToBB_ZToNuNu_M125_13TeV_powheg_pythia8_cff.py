import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISpring15MiniAODv2/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/16624909-C26D-E511-8957-B083FED13C9E.root',
       '/store/mc/RunIISpring15MiniAODv2/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/4C6F6059-C26D-E511-BFE0-0025905C42A6.root',
       '/store/mc/RunIISpring15MiniAODv2/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/6025EC58-C26D-E511-B2D3-0025905C42FE.root',
       '/store/mc/RunIISpring15MiniAODv2/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/70B8FF32-C36D-E511-9280-0025901D4138.root',
       '/store/mc/RunIISpring15MiniAODv2/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/AEF55DF1-C16D-E511-B303-0025907277CE.root',
       '/store/mc/RunIISpring15MiniAODv2/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/B89AF559-C26D-E511-B5E0-0025905BA734.root',
       '/store/mc/RunIISpring15MiniAODv2/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/CAB5545F-C26D-E511-B41A-0025904CF100.root',
       '/store/mc/RunIISpring15MiniAODv2/ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E2FF5F7E-C26D-E511-90D1-0026B9277A4C.root' ] );


secFiles.extend( [
               ] )

