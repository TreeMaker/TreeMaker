import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/24AF6276-C7D2-F84D-9817-CF6FCC447FD1.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/39B1AFF1-1F02-E744-944E-265EFEE05A2C.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/51155E54-BFF1-9449-BBB4-74BC6113B599.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/6196FE14-D2AB-B349-8294-91A1D9F2214F.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/68F972A5-93EF-AA4B-89AD-E715D9ECD610.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/7701BCE7-11D8-924A-B6B9-B78800A1D1CC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/82E5C7C7-E785-5F41-923F-D050DE49D591.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/9C654D78-50B8-A44B-94FF-1B6BEB632A18.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/A34AF657-BCA3-1049-978D-86FBAEFF7394.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/B1438A55-14AD-F645-B3C6-313C5831DE28.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/C4F622F3-2BB1-DF4C-89D5-6F1E70138CD8.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/D675570D-961A-E941-9CE5-8B1F62E48342.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/DDF444A9-4883-7347-A332-90AAE0BEAEFC.root',
       '/store/mc/RunIISummer20UL16MiniAOD/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v2/280000/FFC0F025-64CC-6D41-8F1C-6C1058C31EA3.root',
] )
