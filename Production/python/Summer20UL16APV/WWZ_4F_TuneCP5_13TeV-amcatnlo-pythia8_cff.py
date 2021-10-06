import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/0E22C6EF-980A-D74A-8223-4BF757FC508B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/120000/3118FA49-E53F-ED41-BF40-BA6FBCD4B5E3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/5F3B5D5C-94A5-1F46-89DB-E85C3D23D35F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/C08778C2-2449-B145-B718-C02FB05A13B7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/130000/F315D438-17E6-D040-9EFD-5C822EA0651C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/755AC8AC-30E2-CC4C-A995-6143EF3C5AA8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/140000/E6FDDEBE-6ADE-9D4F-8FAC-7D7DD75FB462.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/3CA02721-4449-3143-A0BB-3E57506CEEAA.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/4875E3AD-56C9-CE4B-86E9-7F238BCABBCC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/270000/D011FEFC-6CA3-DF47-A94B-58F6375EE588.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/7E003B90-1F40-F647-B66C-89F58BD7018B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/ACF92823-609F-B940-9EA3-FE8A26EBA2E0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/C469A8E7-1BE9-2442-A004-A3877D97FE34.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/280000/E7B7AD64-AAA1-8A4E-8ADC-8817D7422DB6.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/53D0DE46-4D0B-D14F-A77C-05AB33B05176.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/742213F5-BF93-4447-BEB2-5B96DBD1F927.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v1/70000/9EA7213C-1BFE-CF4E-92C9-EF6860B9919F.root',
] )
