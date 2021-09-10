import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/BFD27654-FFA4-834B-9BE8-B45000363ABF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/0807B9E0-D1E2-E747-92BC-6C9BBF9E6105.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/130000/CE931FDA-F854-C949-8850-0351731687DF.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/1F374CE8-5C95-4C42-9232-AE5814469DF9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/3224B7AC-CE13-7348-BCAD-0DF7BE3BD37D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/7A6D1106-D505-5B42-AC65-EF501AD5A55B.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/A570C517-B674-F144-AB73-90514597D536.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B1FBFB7E-D2EF-C142-AC6A-8AAEEA290553.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/B20DD357-F7A3-9E4D-9F65-334999607399.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/BDB6BC58-3891-1849-A623-646794BECDC0.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/D0C8C887-35E3-664C-8C2F-916E48F82BB4.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/DA619BE9-0E3B-5345-ACBF-B2A4063E75B5.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/EB4B1C19-27C1-7447-84AD-C8F9A70DCA83.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/0C78819F-CF2A-EC44-98B6-2A5D7809CFFE.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/29EAD60D-FE93-1E47-AF68-A712529A1E8D.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/4FD5CBE6-4AA0-834D-9304-E1A4CEAEA4B3.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/E1B3E71F-1B5C-E94C-B609-3D22F2D044A9.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/F01B5F7B-E0CF-F54B-BBE7-A34BE9A49DEB.root',
       '/store/mc/RunIISummer20UL16MiniAODv2/WZG_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/9226B680-2A6F-BF45-B942-6CE1613C39C3.root',
] )
