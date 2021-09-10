import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/B7703353-7812-2641-9ED3-919644D9B61A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/32F20C62-14A0-754F-ABDE-39D3FBCEA1A6.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/8FF5715C-45CB-5C4B-9F63-B7E4E414A2FE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/0B129C39-34B5-3244-83BC-0CE77212BDAF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/0E73A408-1130-3149-9624-4D23606C8C52.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/43D1C3B5-0AFE-CE45-BA8F-A8A0E2EE1B02.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/6B667CFC-D719-1942-825C-1414CA6BC7F8.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/9B9147ED-893A-8B4B-9188-5D3268B2AAD9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/9BDFEF0A-A908-9848-91C7-EDACE75633F2.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/A643A016-5926-D447-A3E7-0636F5816108.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/D27E2B1A-18D7-564B-9CEC-4AE1F8F1584A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F5F90ADC-1962-D54E-A96C-B1322FFCE443.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/0766EB58-44B1-F449-824F-C0EF63222896.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/CEF497B7-ED9B-4041-8B46-29C0BD04E579.root',
] )
