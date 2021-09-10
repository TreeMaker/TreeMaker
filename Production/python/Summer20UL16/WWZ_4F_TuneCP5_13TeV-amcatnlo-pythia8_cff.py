import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/2DAF66B9-E7D5-DA48-99DF-7C01905A0114.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/11E10D46-AC0B-4940-A893-4C4DDD765882.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3B8792B5-5217-0E42-9238-F1ADDCBD4510.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/CDB02034-0630-DE47-92D1-6241426A8505.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/37441B0C-04A2-6D42-AA74-66E3BB5FC9C7.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/47197573-F618-944E-98D5-C6D2E944E37A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/B1A64E79-6086-8044-8E6C-447F8481270A.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/BD376E74-B00B-AD42-8CA2-4D6AB3C9B99A.root',
] )
